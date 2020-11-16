import enum

class Difficulty(str, enum.Enum):
	easy = "EASY",
	medium = "MEDIUM",
	hard = "HARD"

class Category:
	def __init__(self, name):
		self.name = name

class Player:
	def __init__(self, name):
		self.name = name
		self.statistics = None

class Question:
	def __init__(self, **attr):
		self.question = attr.get("question", "")
		self.answers = attr.get("answers", [])
		self.correct_answer = attr.get("correct_answer", "")
		self.is_correct = False

class Match:
	def __init__(self, questions, category, difficulty = Difficulty.medium):
		self.duration = 0
		self.score = 0
		self.difficulty = difficulty
		self.category = category
		self.questions = questions