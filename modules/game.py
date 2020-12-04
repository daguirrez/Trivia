import graphics as gr
import party as pa
import storage as st
import trivia as tr
import os
from time import time

class Game:
	def __init__(self):
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

	def get_initial_data(self, storage):
		data = {}
		data["players"] = storage.load_players()
		data["categories"] = storage.load_categories()

		return data

	def title_screen(self, storage, data):
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
		pex = [p for p in data["players"] if p.name == player_name]
		if len(pex) > 0:
			return pex[0]
		else:
			# save player
			if not storage.save_player(tr.Player(player_name, None)):
				self.__err_message()

			data["players"] = storage.load_players() # loads players again
			return data["players"][len(data["players"]) - 1]

	def menu_screen(self):
		g = gr.MenuScreen()

		self.__clear_screen()
		print(g.draw())

		while True:
			op = input()

			if op in ("1", "2", "3"):
				# save difficulty
				if op == "1": return tr.Difficulty.easy
				if op == "2": return tr.Difficulty.medium
				if op == "3": return tr.Difficulty.hard

			return None

	def player_stats_screen(self, storage, player):
		statistics = storage.load_player_statistics(player)
		
		g = gr.PlayerStatsScreen(statistics)

		# draw statistics
		self.__clear_screen()
		print(g.draw())
		input() # pause program

		return statistics


	def categories_screen(self, data):
		g = gr.CategoriesScreen(data["categories"])

		self.__clear_screen()
		print(g.draw())

		idc = input()

		# check if exist
		ex = [c for c in data["categories"] if idc == str(c.id)]
		if len(ex) > 0:		return ex[0]
		else:				return data["categories"][0]

	def game_screen(self, category, difficulty, player):
		# make a match
		t = pa.TriviaParty(
			category = category,
			difficulty = difficulty
		)
		m = t.get_match() # get match
		m.player = player

		stime = time() # get start time
		
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

		m.duration = int(time() - stime) # set duration
		return m

	def final_screen(self, storage, match):
		g = gr.FinalScreen(match)

		# save match
		storage.save_match(match)

		# draw
		self.__clear_screen()
		print(g.draw())	
		input() # "pause screen"

	def init_game(self, db = "trivia"):
		storage = st.MyStorage(database = db)

		gdata = self.get_initial_data(storage) # get data from DB
		player = self.title_screen(storage, gdata) # get selected player
		
		while True:
			difficulty = self.menu_screen() # start menu

			if difficulty == None: # see stats
				self.player_stats_screen(storage, player)
				continue
			
			category = self.categories_screen(gdata)
			fmatch = self.game_screen(category, difficulty, player)
			self.final_screen(storage, fmatch)

			gdata = self.get_initial_data(storage) # reestart data




if __name__ == "__main__":
	g = Game()
	g.init_game()