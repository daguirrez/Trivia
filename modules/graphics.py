import abc

class IScreen(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def draw(self):
		pass

class TitleScreen(IScreen):
	def draw(self):
		title = '''
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
		return title

class MenuScreen(IScreen):
	def draw(self):
		menu = '''
		In this game you will be able to experience a 
		trivia of some of the most interesting topics
		currently.

		Menu:
		Play match (writes "to define")
		View player stats(writes "to define")'''
		return menu

class CategoriesScreen(IScreen):
	def __init__(self, categories):
		self.__categories = categories


	def draw(self):
		categories = '''
		Select the category of your trivia. if you 
		don't select any of the default category is 
		Anime & Manga.

		Categories:
		General Knowledge:	writes 9		
		Books:				writes 10
		Films:				writes 11		
		Music:				writes 12		
		Video Games:		writes 15		
		Celebrities:		writes 26
		Animals:			writes 27
		Comics:				writes 29	
		Anime & Manga:		writes 31		
		Cartoon:			writes 32'''
		return categories


class GameScreen(IScreen):
	def draw(self, questions):
		qa = f'''
		Read the question and select the answer you 
		think is right.

		Question: {questions["question"]}
			
		Possible answers:
		{questions["results"]}'''
		return qa

class FinalScreen(IScreen):
	def draw(self, result):
		final1 = '''
		Results:

		╔═╗───╔═╗───╔╗
		║╬╠═╦╦╣═╬═╦═╣╚╗
		║╔╣╩╣╔╣╔╣╩╣═╣╔╣
		╚╝╚═╩╝╚╝╚═╩═╩═╝

		You answered all the questions correctly.

		Do you want to go out or go back to the menu?
		- Enter "" if you want to go back to the menu.
		- Enter "" if you want to exit the game.'''

		final2 = '''
		Results:

		╔═╦╦╗────╔╗
		║║║╠╬═╦═╗║╚╦╦╦╦╗
		║║║║║═╣╩╣║╔╣╔╣║║
		╚╩═╩╩═╩═╝╚═╩╝╠╗║
		─────────────╚═╝

		You answered 7 to 9 correct questions.

		Do you want to go out or go back to the menu?
		- Enter "" if you want to go back to the menu.
		- Enter "" if you want to exit the game.'''

		final3 = '''
		Results:

		╔═╦╗──────────────╔╗──╔╗──╔╗╔╗
		╚╗║╠═╦╦╗╔═╦═╗╔═╦╗╔╝╠═╗║╚╦═╣╚╣╚╦═╦╦╗
		╔╩╗║╬║║║║═╣╬╚╣║║║║╬║╬║║╬║╩╣╔╣╔╣╩╣╔╝
		╚══╩═╩═╝╚═╩══╩╩═╝╚═╩═╝╚═╩═╩═╩═╩═╩╝

		You answered 4 to 6 correct questions.

		Do you want to go out or go back to the menu?
		- Enter "" if you want to go back to the menu.
		- Enter "" if you want to exit the game.'''

		final4 = '''
		Results:

		╔═╦╗────╔═╦╗───────╔╗──────────────────╔╗╔╗
		╚╗║╠═╦╦╗║═╣╚╦═╦╦╦╗╔╝║╔═╦╗╔═╗╔╦╗╔═╗╔═╦╦═╣╚╣╚╦═╦╦╗╔═╦═╗╔══╦═╗
		╔╩╗║╬║║║╠═║║║╬║║║╚╣╬║║╬║╚╣╬╚╣║║║╬╚╣║║║╬║╔╣║║╩╣╔╝║╬║╬╚╣║║║╩╣
		╚══╩═╩═╝╚═╩╩╩═╩═╩═╩═╝║╔╩═╩══╬╗║╚══╩╩═╩═╩═╩╩╩═╩╝─╠╗╠══╩╩╩╩═╝
		─────────────────────╚╝─────╚═╝─────────────────╚═╝

		You answered 1 to 3 correct questions.

		Do you want to go out or go back to the menu?
		- Enter "" if you want to go back to the menu.
		- Enter "" if you want to exit the game.'''

		if result == 10:
			return final1
		
		if result >= 7 and result <= 9:
			return final2
		
		if result >= 4 and result <= 6:
			return final3
		
		return final4