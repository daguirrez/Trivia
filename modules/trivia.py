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
	
	#def get_question(self):
	#	return str(self.question)
	
	#def get_answers(self):
	#	return str(self.answers)

class Match:
	def __init__(self, questions, category, difficulty = Difficulty.medium):
		self.duration = 0
		self.index = 0
		self.player = None
		self.difficulty = difficulty
		self.category = category
		self.questions = questions

	def get_score(self): # pts assigned by difficulty
		score_pts = {
			Difficulty.easy: 1,
			Difficulty.medium: 1.5,
			Difficulty.hard: 2
		}

		qc = len([q for q in self.questions if q.is_correct])
		
		if qc >= 7: # apply multiplier
			qc = int((qc - 7) * score_pts[self.difficulty]) + 7

		return qc

class PlayerStatistics:
	def __init__(self):
		self.wins = 0
		self.games_played = 0
		self.time_played = 0
		self.ranking = -1
		self.best_categories = []