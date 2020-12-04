import graphics as gr
import party as pa
import storage as st
import trivia as tr
import os
from time import time

class Game:
	def __init__(self):
		self.__storage = st.MyStorage()
		self.__players = []
		self.__categories = []
		self.__current_player = None
		self.__gdata = {}

	def __err_message(self):
		print("There was an error in the DB...")
		input() # pause game
		exit(1)

	def __clear_screen(self):
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")

	def get_initial_data(self):
		self.__players = self.__storage.load_players()
		self.__categories = self.__storage.load_categories()

	def title_screen(self):
		g = gr.TitleScreen()
		player_name = str

		# get player name
		while True:
			# print on screen
			self.__clear_screen()
			print(g.draw())

			# get name
			player_name = input().upper()

			if len(player_name.replace(" ", "")) == 3:
				break

		# player exists
		pex = [p for p in self.__players if p.name == player_name]
		if len(pex) > 0:
			self.__current_player = pex[0]
		else:
			# save player
			if not self.__storage.save_player(tr.Player(player_name, None)):
				self.__err_message()

			self.__players = self.__storage.load_players() # loads players again
			self.__current_player = self.__players[len(self.__players) - 1]

	def menu_screen(self):
		g = gr.MenuScreen()

		self.__clear_screen()
		print(g.draw())

		while True:
			op = input()

			if op in ("1", "2", "3"):
				# save difficulty
				if op == "1": self.__gdata["difficulty"] = tr.Difficulty.easy
				if op == "2": self.__gdata["difficulty"] = tr.Difficulty.medium
				if op == "3": self.__gdata["difficulty"] = tr.Difficulty.hard

				return "categories"
			if op == "4":
				return "stats"

	def player_stats_screen(self):
		g = gr.PlayerStatsScreen(self.__storage.load_player_statistics(self.__current_player))

		# draw statistics
		self.__clear_screen()
		print(g.draw())
		input() # pause program


	def categories_screen(self):
		g = gr.CategoriesScreen(self.__categories)

		self.__clear_screen()
		print(g.draw())

		idc = input()

		# check if exist
		ex = [c for c in self.__categories if idc == str(c.id)]
		if len(ex) > 0:		self.__gdata["category"] = ex[0]
		else:				self.__gdata["category"] = self.__categories[0]

	def game_screen(self):
		# make a match
		t = pa.TriviaParty(
			category = self.__gdata["category"],
			difficulty = self.__gdata["difficulty"]
		)
		m = t.get_match() # get match
		m.player = self.__current_player

		self.__gdata["stime"] = time() # get start time
		
		g = gr.GameScreen(m)

		for k in range(len(m.questions)):
			m.index = k
			
			self.__clear_screen()
			print(g.draw()) # draw

			answer = input() # get user answer

			try:
				answer = int(answer)

				if answer > len(m.questions[k].answers):
					answer = 1
			except Exception:
				answer = 1

			# check answer
			m.questions[k].is_correct = (m.questions[k].answers[answer - 1] == m.questions[k].correct_answer)

		self.__gdata["match"] = m

	def final_screen(self):
		m = self.__gdata["match"]
		g = gr.FinalScreen(m)

		# save match
		m.duration = int(time() - self.__gdata["stime"])
		self.__storage.save_match(m)

		# draw
		self.__clear_screen()
		print(g.draw())	
		input() # "pause screen"

	def init_game(self):
		self.get_initial_data() # inits game
		self.title_screen()
		
		while True:
			menu_o = self.menu_screen() # start menu

			if menu_o == "stats": # see stats
				self.player_stats_screen()
				continue
			
			self.categories_screen()
			self.game_screen()
			self.final_screen()

			self.get_initial_data() # reestart data




if __name__ == "__main__":
	g = Game()
	g.init_game()