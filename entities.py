# == ENTITIES ==
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

class EDifficulty:
	EASY = 0,
	MEDIUM = 1,
	HARD = 2

class Match:
	def __init__(self, questions):
		self.duration = 0
		self.score = 0
		self.difficulty = EDifficulty.MEDIUM
		self.questions = questions

# == INTERFACES ==
class IStatistics:
	def load_data(self):
		pass

	def save_data(self):
		pass

class IScreen:
	def draw(self):
		pass

class IParty:
	def get_match(self): # RETURN MATCH OBJECT
		pass