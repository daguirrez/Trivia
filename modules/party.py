import abc
import requests
import random
from urllib.parse import unquote
from trivia import Difficulty, Question, Category, Match

class IParty(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def get_match(self):
		pass


class TriviaParty(IParty):
	def __init__(self, **settings):
		self.__category = settings.get("category", Category("Anime & Manga"))
		self.__difficulty = settings.get("difficulty", Difficulty.medium)

	def __get_category_api_id(self):
		return {
			"Books":			"10",		# Entertainment: Books
			"Film":				"11",		# Entertainment: Film
			"Music":			"12",		# Entertainment: Music
			"Video Games":		"15",		# Entertainment: Video Games
			"Celebrities":		"26",		# Celebrities
			"Animals":			"27",		# Animals
			"Comics":			"29",		# Entertainment: Comics
			"Anime & Manga":	"31",		# Entertainment: Japanese Anime & Manga
			"Cartoon":			"32"		# Entertainment: Cartoon & Animations
		}.get(self.__category.name, "-1")	# Default: Nothing

	def get_match(self):
		# url params: amount=10&category=""&difficulty=""&type=multiple&encode=base64
		url = f"https://opentdb.com/api.php?amount=10&category={self.__get_category_api_id()}&difficulty={self.__difficulty.lower()}&type=multiple&encode=url3986"
		data = {}
		
		# call the API Open Trivia DB
		try:
			response = requests.get(url)
			data = response.json()
		except requests.exceptions.RequestException:
			return None

		# check if has an error
		if data["response_code"] != 0:
			return None

		# convert data to match object
		questions = [Question(
			question 		= unquote(r["question"]),
			answers			= [unquote(a) for a in r["incorrect_answers"]],
			correct_answer	= unquote(r["correct_answer"])
		) for r in data["results"]]

		for q in questions:
			q.answers.append(q.correct_answer)
			random.shuffle(q.answers)

		return Match(questions, self.__category, self.__difficulty)


