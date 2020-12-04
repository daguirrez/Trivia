import unittest
import mysql.connector
from unittest.mock import Mock, MagicMock, patch
from game import Game
import graphics as gr
import party as pa
import storage as st
import trivia as tr

class GameITest(unittest.TestCase):
	def __select_into_db(self, query):
		db = mysql.connector.connect(
			host		= "localhost",
			user		= "root",
			password	= "",
			database	= "trivia_test"
		)
		
		with db.cursor() as cursor:
			cursor.execute(query)
			return cursor.fetchall()

	def __call_sql_file(self, path):
		db = mysql.connector.connect(
			host		= "localhost",
			user		= "root",
			password	= ""
		)
		with open(f"../database/{path}", "r") as f:
			with db.cursor() as cursor:
				directives = f.read().split(";")

				for di in directives:
					if di.strip() != "":
						cursor.execute(di)
			
			db.commit()

	def __start_database(self):
		self.__call_sql_file("create_trivia_t.sql") # create integration test database

	def __finish_database(self):
		self.__call_sql_file("drop_trivia_t.sql") # drop integration test database

	def test_initial_data(self):
		# expected data
		ex_categories = [
			tr.Category('General Knowledge',	1),
			tr.Category('Books',				2),
			tr.Category('Film',					3),
			tr.Category('Music',				4),
			tr.Category('Video Games',			5),
			tr.Category('Celebrities',			6),
			tr.Category('Animals',				7),
			tr.Category('Comics',				8),
			tr.Category('Anime & Manga',		9),
			tr.Category('Cartoon',				10)
		]
		ex_players = [
			tr.Player('DAN', 1),
			tr.Player('DAV', 2)
		]

		self.__start_database()
		
		g = Game()
		storage = st.MyStorage(database = "trivia_test")
		data = g.get_initial_data(storage)
		
		self.__finish_database()

		# check categories
		for k in range(len(ex_categories)):
			self.assertEqual(ex_categories[k].id, data["categories"][k].id)
			self.assertEqual(ex_categories[k].name, data["categories"][k].name)

		# check players
		for k in range(len(ex_players)):
			self.assertEqual(ex_players[k].id, data["players"][k].id)
			self.assertEqual(ex_players[k].name, data["players"][k].name)

	@patch("builtins.print")
	@patch("builtins.input")
	@patch("os.system")
	def test_title_screen(self, mock_os, mock_input, mock_print):
		tests = [
			{
				"input": "dav",
				"ex_player": tr.Player("DAV", 2),
				"db": [
					(1, "DAN"),
					(2, "DAV")
				]
			},
			{
				"input": "new",
				"ex_player": tr.Player("NEW", 3),
				"db": [
					(1, "DAN"),
					(2, "DAV"),
					(3, "NEW")
				]
			}
		]

		self.__start_database()
		
		g = Game()
		storage = st.MyStorage(database = "trivia_test")
		data = g.get_initial_data(storage) # get data

		for t in tests:
			mock_input.return_value = t["input"] # add input
			res_player = g.title_screen(storage, data)

			# check expected player
			self.assertEqual(res_player.id, t["ex_player"].id)
			self.assertEqual(res_player.name, t["ex_player"].name)

			# check data into database
			res_db = self.__select_into_db("SELECT * FROM players")
			self.assertCountEqual(res_db, t["db"])

		self.__finish_database()

	@patch("builtins.print")
	@patch("builtins.input")
	@patch("os.system")
	def test_player_stats_screen(self, mock_os, mock_input, mock_print):
		tests = [
			{
				"player": tr.Player("DAN", 1),
				"ex_stats": tr.PlayerStatistics(
					wins = 0,
					games_played = 3,
					time_played = 95,
					ranking = 1,
					best_categories = [1, 9]
				)
			},
			{
				"player": tr.Player("DAV", 2),
				"ex_stats": tr.PlayerStatistics(
					wins = 0,
					games_played = 2,
					time_played = 93,
					ranking = 2,
					best_categories = [8, 1]
				)
			}
		]

		self.__start_database()
		
		g = Game()
		storage = st.MyStorage(database = "trivia_test")

		for t in tests:
			res_stats = g.player_stats_screen(storage, t["player"])

			# check statistics
			self.assertEqual(res_stats.wins,			t["ex_stats"].wins)
			self.assertEqual(res_stats.games_played,	t["ex_stats"].games_played)
			self.assertEqual(res_stats.time_played,		t["ex_stats"].time_played)
			self.assertEqual(res_stats.ranking,			t["ex_stats"].ranking)
			
			# check categories
			for k in range(len(t["ex_stats"].best_categories)):
				self.assertEqual(res_stats.best_categories[k].id, t["ex_stats"].best_categories[k])

		self.__finish_database()

	@patch("builtins.print")
	@patch("builtins.input")
	@patch("os.system")
	def test_final_screen(self, mock_os, mock_input, mock_print):
		tests = [
			{
				"match_to_save": tr.Match(
					[
						tr.Question(question = "question_one", answers = ["y", "n"], is_correct = True),
						tr.Question(question = "question_two", answers = ["y", "n"], is_correct = True),
						tr.Question(question = "question_three", answers = ["y", "n"], is_correct = False)
					],
					tr.Category("", 2),
					tr.Difficulty.easy
				),
				"player": tr.Player("DAN", 1),
				"id_inserted": 6,
				# id, duration, score, id_player, id_category, difficulty
				"db": (6, 0, 2, 1, 2, 'EASY')
			},
			{
				"match_to_save": tr.Match(
					[
						tr.Question(question = "question_one", answers = ["y", "n"], is_correct = True),
						tr.Question(question = "question_two", answers = ["y", "n"], is_correct = False),
						tr.Question(question = "question_three", answers = ["y", "n"], is_correct = False)
					],
					tr.Category("", 1),
					tr.Difficulty.hard
				),
				"player": tr.Player("DAV", 2),
				"id_inserted": 7,
				# id, duration, score, id_player, id_category, difficulty
				"db": (7, 0, 1, 2, 1, 'HARD')
			},
			{
				"match_to_save": tr.Match(
					[],
					tr.Category("", 3),
					tr.Difficulty.medium
				),
				"player": tr.Player("DAV", 2),
				"id_inserted": 8,
				# id, duration, score, id_player, id_category, difficulty
				"db": (8, 0, 0, 2, 3, 'MEDIUM')
			}
		]

		self.__start_database()
		
		g = Game()
		storage = st.MyStorage(database = "trivia_test")

		for t in tests:
			t["match_to_save"].player = t["player"]
			g.final_screen(storage, t["match_to_save"]) # match saved

			# check data into database
			imatch = self.__select_into_db(f"SELECT * FROM matches WHERE id={t['id_inserted']}")[0]
			
			self.assertCountEqual(imatch, t["db"])

		self.__finish_database()

if __name__ == "__main__":
	unittest.main()