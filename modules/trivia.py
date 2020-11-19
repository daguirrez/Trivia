import enum

class Difficulty(str, enum.Enum):
	easy = "EASY",
	medium = "MEDIUM",
	hard = "HARD"

class Category:
	def __init__(self, name, id = None):
		self.name = name
		self.__id = id

	@property
	def id(self):
		return self.__id


class Player:
	def __init__(self, name, id = None):
		self.name = name
		self.__id = id

	@property
	def id(self):
		return self.__id

class Question:
	def __init__(self, **attr):
		self.question = attr.get("question", "")
		self.answers = attr.get("answers", [])
		self.correct_answer = attr.get("correct_answer", "")
		self.is_correct = False

class Match:
	def __init__(self, questions, category, difficulty = Difficulty.medium):
		self.duration = 0
		self.player = None
		self.difficulty = difficulty
		self.category = category
		self.questions = questions

	def get_score(self):
		return len([q for q in self.questions if q.is_correct])