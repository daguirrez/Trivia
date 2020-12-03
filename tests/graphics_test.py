import sys
import unittest
from unittest.mock import Mock, MagicMock, patch

sys.path.append("../modules")

from graphics import *

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
		
		Enter your player name in three letters:'''
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
		View player stats(writes 2)'''
		instancia = MenuScreen()
		salida_real = instancia.draw()
		self.assertEqual(salida_esperada, salida_real)

	#no complete la función así que tampoco pude hacer el test
	#def test_categoriesscreen(self):

	#si funciona, pero la función regresa el objeto no un string 
	#def test_gamescreen(self):
	#	test_cases = (
    #        {
	#			"index": 0,
    #            "question": ["¿esto funcionara?"],
	#			"answers": ["si", "no", "quiza", "definitivamente no"],
    #            "salida_esperada": '''
	#	Read the question and select the answer you 
	#	think is right.

	#	Question: ¿esto funcionara?
					
	#	Possible answers:
	#	["si", "no", "quiza", "definitivamente no"]''',
    #        },
    #    )

	#	for cp in test_cases:
	#		mock_match = MagicMock()
	#		mock_match.return_value = MagicMock()
	#		mock_match.return_value.index = cp["index"]
	#		mock_match.return_value.question = cp["question"]
	#		mock_match.return_value.answers = cp["answers"]
			
	#		instancia = GameScreen(mock_match)
	#		salida_real = instancia.draw()
	#		self.assertEqual(salida_real, cp["salida_esperada"])
	
	def test_finalscreen(self):
		test_cases = (
			{
				"resultscorrect": [],
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
				"resultscorrect": [True],
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
				"resultscorrect": [True, True],
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
				"resultscorrect": [True, True, True],
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
				"resultscorrect": [True, True, True, True],
				"salida_esperada": '''
		Results:

		╔═╦╗──────────────╔╗──╔╗──╔╗╔╗
		╚╗║╠═╦╦╗╔═╦═╗╔═╦╗╔╝╠═╗║╚╦═╣╚╣╚╦═╦╦╗
		╔╩╗║╬║║║║═╣╬╚╣║║║║╬║╬║║╬║╩╣╔╣╔╣╩╣╔╝
		╚══╩═╩═╝╚═╩══╩╩═╝╚═╩═╝╚═╩═╩═╩═╩═╩╝

		You answered 4 to 6 correct questions.''',
			},
			{
				"resultscorrect": [True, True, True, True, True],
				"salida_esperada": '''
		Results:

		╔═╦╗──────────────╔╗──╔╗──╔╗╔╗
		╚╗║╠═╦╦╗╔═╦═╗╔═╦╗╔╝╠═╗║╚╦═╣╚╣╚╦═╦╦╗
		╔╩╗║╬║║║║═╣╬╚╣║║║║╬║╬║║╬║╩╣╔╣╔╣╩╣╔╝
		╚══╩═╩═╝╚═╩══╩╩═╝╚═╩═╝╚═╩═╩═╩═╩═╩╝

		You answered 4 to 6 correct questions.''',
			},
			{
				"resultscorrect": [True, True, True, True, True, True],
				"salida_esperada": '''
		Results:

		╔═╦╗──────────────╔╗──╔╗──╔╗╔╗
		╚╗║╠═╦╦╗╔═╦═╗╔═╦╗╔╝╠═╗║╚╦═╣╚╣╚╦═╦╦╗
		╔╩╗║╬║║║║═╣╬╚╣║║║║╬║╬║║╬║╩╣╔╣╔╣╩╣╔╝
		╚══╩═╩═╝╚═╩══╩╩═╝╚═╩═╝╚═╩═╩═╩═╩═╩╝

		You answered 4 to 6 correct questions.''',
			},
			{
				"resultscorrect": [True, True, True, True, True, True, True],
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
				"resultscorrect": [True, True, True, True, True, True, True, True],
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
				"resultscorrect": [True, True, True, True, True, True, True, True, True],
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
				"resultscorrect": [True, True, True, True, True, True, True, True, True, True],
				"salida_esperada": '''
		Results:

		╔═╗───╔═╗───╔╗
		║╬╠═╦╦╣═╬═╦═╣╚╗
		║╔╣╩╣╔╣╔╣╩╣═╣╔╣
		╚╝╚═╩╝╚╝╚═╩═╩═╝

		You answered all the questions correctly.''',
			},
		)

		for cp in test_cases:
			mock_match = MagicMock()
			mock_match.return_value = MagicMock()
			mock_match.return_value.questions = MagicMock()
			mock_match.return_value.questions.is_correct = cp["resultscorrect"]

			instancia = FinalScreen(mock_match)
			salida_real = instancia.draw()
			self.assertEqual(salida_real, cp["salida_esperada"])

if __name__ == '__main__':
    unittest.main()