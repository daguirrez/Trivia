import abc
from trivia import Category, Match, PlayerStatistics

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
		
		Enter your player name in three letters:
		'''
		return title

class MenuScreen(IScreen):
	def draw(self):
		return '''
		In this game you will be able to experience a 
		trivia of some of the most interesting topics
		currently.

		Menu:
		Play easy match (writes 1)
		Play medium match (writes 2)
		Play hard match (writes 3)
		View player stats(writes 4)
		'''

class PlayerStatsScreen(IScreen):
	def __init__(self, player_stats):
		self.player_stats = player_stats
	
	def draw(self):
		if self.player_stats == None:
			return "You don't have statistics"

		k = 0
		categories = "\n\t\t".join([str(k := k + 1) + ". " + c.name for c in self.player_stats.best_categories])

		return f'''
		Your stats are:

		Wins: {self.player_stats.wins}
		Games played: {self.player_stats.games_played}
		Time played: {self.player_stats.time_played}s
		Ranking: #{self.player_stats.ranking}
		
		Best categories:
		{categories}
		'''

class CategoriesScreen(IScreen):
	def __init__(self, categories):
		self.__categories = categories

	def draw(self):
		categories = "\n\t\t".join([(q.name + " writes " + str(q.id)) for q in self.__categories])

		return f'''
		Select the category of your trivia. if you 
		don't select any of the default category is 
		Anime & Manga. (Introduce the id)

		Categories:
		{categories}
		'''

class GameScreen(IScreen):
	def __init__(self, match):
		self.__match = match

	def draw(self):
		k = 0
		answers = "\n\t\t".join([str(k := k + 1) + ". " + a for a in self.__match.questions[self.__match.index].answers])
		
		return f'''
		Read the question and select the answer you 
		think is right.

		Question:
		{self.__match.questions[self.__match.index].question}

		Possible answers:
		{answers}
		'''

class FinalScreen(IScreen):
	def __init__(self, match):
		self.__match = match

	def draw(self):
		# get result
		result = len([q for q in self.__match.questions if q.is_correct])
		
		final1 = '''
		Results:

		╔═╗───╔═╗───╔╗
		║╬╠═╦╦╣═╬═╦═╣╚╗
		║╔╣╩╣╔╣╔╣╩╣═╣╔╣
		╚╝╚═╩╝╚╝╚═╩═╩═╝

		You answered all the questions correctly.'''

		final2 = '''
		Results:

		╔═╦╦╗────╔╗
		║║║╠╬═╦═╗║╚╦╦╦╦╗
		║║║║║═╣╩╣║╔╣╔╣║║
		╚╩═╩╩═╩═╝╚═╩╝╠╗║
		─────────────╚═╝

		You answered 7 to 9 correct questions.'''

		final3 = '''
		Results:

		╔═╦╗──────────────╔╗──╔╗──╔╗╔╗
		╚╗║╠═╦╦╗╔═╦═╗╔═╦╗╔╝╠═╗║╚╦═╣╚╣╚╦═╦╦╗
		╔╩╗║╬║║║║═╣╬╚╣║║║║╬║╬║║╬║╩╣╔╣╔╣╩╣╔╝
		╚══╩═╩═╝╚═╩══╩╩═╝╚═╩═╝╚═╩═╩═╩═╩═╩╝

		You answered 4 to 6 correct questions.'''

		final4 = '''
		Results:

		╔═╦╗────╔═╦╗───────╔╗──────────────────╔╗╔╗
		╚╗║╠═╦╦╗║═╣╚╦═╦╦╦╗╔╝║╔═╦╗╔═╗╔╦╗╔═╗╔═╦╦═╣╚╣╚╦═╦╦╗╔═╦═╗╔══╦═╗
		╔╩╗║╬║║║╠═║║║╬║║║╚╣╬║║╬║╚╣╬╚╣║║║╬╚╣║║║╬║╔╣║║╩╣╔╝║╬║╬╚╣║║║╩╣
		╚══╩═╩═╝╚═╩╩╩═╩═╩═╩═╝║╔╩═╩══╬╗║╚══╩╩═╩═╩═╩╩╩═╩╝─╠╗╠══╩╩╩╩═╝
		─────────────────────╚╝─────╚═╝─────────────────╚═╝

		You answered 1 to 3 correct questions.'''

		if result == 10:
			return final1
		
		if result >= 7 and result <= 9:
			return final2
		
		if result >= 4 and result <= 6:
			return final3
		
		return final4

