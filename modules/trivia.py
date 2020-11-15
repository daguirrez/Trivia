import enum

class Difficulty(str, enum.Enum):
	EASY = "EASY",
	MEDIUM = "MEDIUM",
	HARD = "HARD"

class Category:
	def __init__(self, name):
		self.name = name

class Player:
	def __init__(self, name):
		self.name = name
		self.statistics = None

class Question:
	def __init__(self, **kargs):
		self.question = kargs.get("question", "")
		self.answers = kargs.get("answers", [])
		self.correct_answer = kargs.get("correct_answer", "")
		self.is_correct = False

class Match:
	def __init__(self, questions):
		self.duration = 0
		self.score = 0
		self.difficulty = Difficulty.MEDIUM
		self.questions = questions