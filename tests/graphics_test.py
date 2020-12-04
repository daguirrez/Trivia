import sys
import unittest
from unittest.mock import Mock, MagicMock, patch

sys.path.append("../modules")

from graphics import *
from trivia import *

class GraphicsTest(unittest.TestCase):
	def test_titlescreen(self):
		salida_esperada = '''
		───────────────────────────────────────────────────────────────────────────────────────
		─██████████████─████████████████───██████████─██████──██████─██████████─██████████████─
		─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░██─██░░██──██░░██─██░░░░░░██─██░░░░░░░░░░██─
		─██████░░██████─██░░████████░░██───████░░████─██░░██──██░░██─████░░████─██░░██████░░██─
		─────██░░██─────██░░██────██░░██─────██░░██───██░░██──██░░██───██░░██───██░░██──██░░██─
		─────██░░██─────██░░████████░░██─────██░░██───██░░██──██░░██───██░░██───██░░██████░░██─
		─────██░░██─────██░░░░░░░░░░░░██─────██░░██───██░░██──██░░██───██░░██───██░░░░░░░░░░██─
		─────██░░██─────██░░██████░░████─────██░░██───██░░██──██░░██───██░░██───██░░██████░░██─
		─────██░░██─────██░░██──██░░██───────██░░██───██░░░░██░░░░██───██░░██───██░░██──██░░██─
		─────██░░██─────██░░██──██░░██████─████░░████─████░░░░░░████─████░░████─██░░██──██░░██─
		─────██░░██─────██░░██──██░░░░░░██─██░░░░░░██───████░░████───██░░░░░░██─██░░██──██░░██─
		─────██████─────██████──██████████─██████████─────██████─────██████████─██████──██████─
		───────────────────────────────────────────────────────────────────────────────────────
		────────────────────────────────────────────────────────────────────────
		─██████████████─██████████─██████──────────██████─██████████████─██████─
		─██░░░░░░░░░░██─██░░░░░░██─██░░██████████████░░██─██░░░░░░░░░░██─██░░██─
		─██████░░██████─████░░████─██░░░░░░░░░░░░░░░░░░██─██░░██████████─██░░██─
		─────██░░██───────██░░██───██░░██████░░██████░░██─██░░██─────────██░░██─
		─────██░░██───────██░░██───██░░██──██░░██──██░░██─██░░██████████─██░░██─
		─────██░░██───────██░░██───██░░██──██░░██──██░░██─██░░░░░░░░░░██─██░░██─
		─────██░░██───────██░░██───██░░██──██████──██░░██─██░░██████████─██████─
		─────██░░██───────██░░██───██░░██──────────██░░██─██░░██────────────────
		─────██░░██─────████░░████─██░░██──────────██░░██─██░░██████████─██████─
		─────██░░██─────██░░░░░░██─██░░██──────────██░░██─██░░░░░░░░░░██─██░░██─
		─────██████─────██████████─██████──────────██████─██████████████─██████─
		────────────────────────────────────────────────────────────────────────
		
		Enter your player name in three letters:
		'''

		instancia = TitleScreen()
		salida_real = instancia.draw()
		self.assertEqual(salida_esperada, salida_real)
	
	def test_menuscreen(self):
		salida_esperada = '''
		In this game you will be able to experience a 
		trivia of some of the most interesting topics
		currently.

		Menu:
		Play match (writes 1)
		View player stats(writes 2)
		'''

		instancia = MenuScreen()
		salida_real = instancia.draw()
		self.assertEqual(salida_esperada, salida_real)

	def test_gamescreen(self):
		test_cases = [
			{
				"index": 0,
				"questions": [
					Question(
						question = "¿esto funcionara?",
						answers = ["si", "no", "quiza", "definitivamente no"]
					)
				],
				"salida_esperada": '''
		Read the question and select the answer you 
		think is right.

		Question:
		¿esto funcionara?

		Possible answers:
		si
		no
		quiza
		definitivamente no
		'''
			},
			{
				"index": 1,
				"questions": [
					Question(
						question = "¿esto funcionara?",
						answers = ["si", "no", "quiza", "definitivamente no"]
					),
					Question(
						question = "¿esto funcionara 2?",
						answers = ["si", "no"]
					)
				],
				"salida_esperada": '''
		Read the question and select the answer you 
		think is right.

		Question:
		¿esto funcionara 2?

		Possible answers:
		si
		no
		'''
			}
		]

		for t in test_cases:
			m = Match(t["questions"], None)
			m.index = t["index"]

			instancia = GameScreen(m)
			salida_real = instancia.draw()
			self.assertEqual(salida_real, t["salida_esperada"])
	
	def test_finalscreen(self):
		test_cases = (
			{
				"questions": [Question(is_correct = False)],
				"salida_esperada": '''
		Results:

		╔═╦╗────╔═╦╗───────╔╗──────────────────╔╗╔╗
		╚╗║╠═╦╦╗║═╣╚╦═╦╦╦╗╔╝║╔═╦╗╔═╗╔╦╗╔═╗╔═╦╦═╣╚╣╚╦═╦╦╗╔═╦═╗╔══╦═╗
		╔╩╗║╬║║║╠═║║║╬║║║╚╣╬║║╬║╚╣╬╚╣║║║╬╚╣║║║╬║╔╣║║╩╣╔╝║╬║╬╚╣║║║╩╣
		╚══╩═╩═╝╚═╩╩╩═╩═╩═╩═╝║╔╩═╩══╬╗║╚══╩╩═╩═╩═╩╩╩═╩╝─╠╗╠══╩╩╩╩═╝
		─────────────────────╚╝─────╚═╝─────────────────╚═╝

		You answered 1 to 3 correct questions.''',
			},
			{
				"questions": [Question(is_correct = True), Question(is_correct = False)],
				"salida_esperada": '''
		Results:

		╔═╦╗────╔═╦╗───────╔╗──────────────────╔╗╔╗
		╚╗║╠═╦╦╗║═╣╚╦═╦╦╦╗╔╝║╔═╦╗╔═╗╔╦╗╔═╗╔═╦╦═╣╚╣╚╦═╦╦╗╔═╦═╗╔══╦═╗
		╔╩╗║╬║║║╠═║║║╬║║║╚╣╬║║╬║╚╣╬╚╣║║║╬╚╣║║║╬║╔╣║║╩╣╔╝║╬║╬╚╣║║║╩╣
		╚══╩═╩═╝╚═╩╩╩═╩═╩═╩═╝║╔╩═╩══╬╗║╚══╩╩═╩═╩═╩╩╩═╩╝─╠╗╠══╩╩╩╩═╝
		─────────────────────╚╝─────╚═╝─────────────────╚═╝

		You answered 1 to 3 correct questions.''',
			},
			{
				"questions": [Question(is_correct = True)] * 2,
				"salida_esperada": '''
		Results:

		╔═╦╗────╔═╦╗───────╔╗──────────────────╔╗╔╗
		╚╗║╠═╦╦╗║═╣╚╦═╦╦╦╗╔╝║╔═╦╗╔═╗╔╦╗╔═╗╔═╦╦═╣╚╣╚╦═╦╦╗╔═╦═╗╔══╦═╗
		╔╩╗║╬║║║╠═║║║╬║║║╚╣╬║║╬║╚╣╬╚╣║║║╬╚╣║║║╬║╔╣║║╩╣╔╝║╬║╬╚╣║║║╩╣
		╚══╩═╩═╝╚═╩╩╩═╩═╩═╩═╝║╔╩═╩══╬╗║╚══╩╩═╩═╩═╩╩╩═╩╝─╠╗╠══╩╩╩╩═╝
		─────────────────────╚╝─────╚═╝─────────────────╚═╝

		You answered 1 to 3 correct questions.''',
			},
			{
				"questions": [Question(is_correct = True)] * 3,
				"salida_esperada": '''
		Results:

		╔═╦╗────╔═╦╗───────╔╗──────────────────╔╗╔╗
		╚╗║╠═╦╦╗║═╣╚╦═╦╦╦╗╔╝║╔═╦╗╔═╗╔╦╗╔═╗╔═╦╦═╣╚╣╚╦═╦╦╗╔═╦═╗╔══╦═╗
		╔╩╗║╬║║║╠═║║║╬║║║╚╣╬║║╬║╚╣╬╚╣║║║╬╚╣║║║╬║╔╣║║╩╣╔╝║╬║╬╚╣║║║╩╣
		╚══╩═╩═╝╚═╩╩╩═╩═╩═╩═╝║╔╩═╩══╬╗║╚══╩╩═╩═╩═╩╩╩═╩╝─╠╗╠══╩╩╩╩═╝
		─────────────────────╚╝─────╚═╝─────────────────╚═╝

		You answered 1 to 3 correct questions.''',
			},
			{
				"questions": [Question(is_correct = True)] * 4,
				"salida_esperada": '''
		Results:

		╔═╦╗──────────────╔╗──╔╗──╔╗╔╗
		╚╗║╠═╦╦╗╔═╦═╗╔═╦╗╔╝╠═╗║╚╦═╣╚╣╚╦═╦╦╗
		╔╩╗║╬║║║║═╣╬╚╣║║║║╬║╬║║╬║╩╣╔╣╔╣╩╣╔╝
		╚══╩═╩═╝╚═╩══╩╩═╝╚═╩═╝╚═╩═╩═╩═╩═╩╝

		You answered 4 to 6 correct questions.''',
			},
			{
				"questions": [Question(is_correct = True)] * 5,
				"salida_esperada": '''
		Results:

		╔═╦╗──────────────╔╗──╔╗──╔╗╔╗
		╚╗║╠═╦╦╗╔═╦═╗╔═╦╗╔╝╠═╗║╚╦═╣╚╣╚╦═╦╦╗
		╔╩╗║╬║║║║═╣╬╚╣║║║║╬║╬║║╬║╩╣╔╣╔╣╩╣╔╝
		╚══╩═╩═╝╚═╩══╩╩═╝╚═╩═╝╚═╩═╩═╩═╩═╩╝

		You answered 4 to 6 correct questions.''',
			},
			{
				"questions": [Question(is_correct = True)] * 6,
				"salida_esperada": '''
		Results:

		╔═╦╗──────────────╔╗──╔╗──╔╗╔╗
		╚╗║╠═╦╦╗╔═╦═╗╔═╦╗╔╝╠═╗║╚╦═╣╚╣╚╦═╦╦╗
		╔╩╗║╬║║║║═╣╬╚╣║║║║╬║╬║║╬║╩╣╔╣╔╣╩╣╔╝
		╚══╩═╩═╝╚═╩══╩╩═╝╚═╩═╝╚═╩═╩═╩═╩═╩╝

		You answered 4 to 6 correct questions.''',
			},
			{
				"questions": [Question(is_correct = True)] * 7,
				"salida_esperada": '''
		Results:

		╔═╦╦╗────╔╗
		║║║╠╬═╦═╗║╚╦╦╦╦╗
		║║║║║═╣╩╣║╔╣╔╣║║
		╚╩═╩╩═╩═╝╚═╩╝╠╗║
		─────────────╚═╝

		You answered 7 to 9 correct questions.''',
			},
			{
				"questions": [Question(is_correct = True)] * 8,
				"salida_esperada": '''
		Results:

		╔═╦╦╗────╔╗
		║║║╠╬═╦═╗║╚╦╦╦╦╗
		║║║║║═╣╩╣║╔╣╔╣║║
		╚╩═╩╩═╩═╝╚═╩╝╠╗║
		─────────────╚═╝

		You answered 7 to 9 correct questions.''',
			},
			{
				"questions": [Question(is_correct = True)] * 9,
				"salida_esperada": '''
		Results:

		╔═╦╦╗────╔╗
		║║║╠╬═╦═╗║╚╦╦╦╦╗
		║║║║║═╣╩╣║╔╣╔╣║║
		╚╩═╩╩═╩═╝╚═╩╝╠╗║
		─────────────╚═╝

		You answered 7 to 9 correct questions.''',
			},
			{
				"questions": [Question(is_correct = True)] * 10,
				"salida_esperada": '''
		Results:

		╔═╗───╔═╗───╔╗
		║╬╠═╦╦╣═╬═╦═╣╚╗
		║╔╣╩╣╔╣╔╣╩╣═╣╔╣
		╚╝╚═╩╝╚╝╚═╩═╩═╝

		You answered all the questions correctly.''',
			},
		)

		for t in test_cases:
			m = Match(t["questions"], None)
			instance = FinalScreen(m)

			salida_real = instance.draw()
			self.assertEqual(salida_real, t["salida_esperada"])

	def test_stats_screen(self):
		ex_output = '''
		Your stats are:

		Wins: 5
		Games played: 20
		Time played: 56s
		Ranking: #2
		
		Best categories:
		Books
		Films
		'''

		ps = PlayerStatistics()

		ps.wins = 5
		ps.games_played = 20
		ps.time_played = 56
		ps.ranking = 2
		ps.best_categories = [Category("Books"), Category("Films")]

		title = PlayerStatsScreen(ps)

		r_output = title.draw()
		self.assertEqual(ex_output, r_output)

	def test_categories(self):
		ex_output = '''
		Select the category of your trivia. if you 
		don't select any of the default category is 
		Anime & Manga. (Introduce the id)

		Categories:
		Books writes 1
		Films writes 2
		Games writes 3
		'''

		title = CategoriesScreen([
			Category("Books", 1),
			Category("Films", 2),
			Category("Games", 3)
		])

		r_output = title.draw()
		self.assertEqual(ex_output, r_output)

if __name__ == '__main__':
    unittest.main()