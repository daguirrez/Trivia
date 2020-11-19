import abc
import mysql.connector
from trivia import Player

class IStorage(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def save_player(self, player):
		pass
	
	@abc.abstractmethod
	def save_match(self, match):
		pass

	@abc.abstractmethod
	def load_players(self):
		pass


class MyStorage(IStorage):
	def __connect(self):
		# connect with the database
		return mysql.connector.connect(
			host		= "localhost",
			user		= "root",
			password	= "",
			database	= "trivia"
		)

	def __close(self, db, cursor):
		# close connections
		if cursor != None:
			cursor.close()

		if db != None and db.is_connected():
			db.close()

	def __insert(self, query, values):
		db = c = None

		try:
			# set connection
			db = self.__connect()
			c = db.cursor()

			# save data
			c.execute(query, values)
			db.commit()

			return c.rowcount > 0
		except mysql.connector.Error:
			return False
		finally:
			self.__close(db, c)

	def __select(self, query, values = None, select_one = False):
		db = c = None

		try:
			# set connection
			db = self.__connect()
			c = db.cursor()

			# save data
			c.execute(query, values)
			
			if select_one:	result = c.fetchone()
			else:			result = c.fetchall()

			return result
		except mysql.connector.Error as e:
			return [] if not select_one else None
		finally:
			self.__close(db, c)


	def save_player(self, player):
		return self.__insert(
			"""
			REPLACE INTO players (
				id,
				name
			) VALUES (%s, %s)
			""",
			(
				player.id,
				player.name
			)
		)

	def save_match(self, match):
		return self.__insert(
			"""
			INSERT INTO matches (
				duration,
				score,
				id_player,
				id_category,
				difficulty
			) VALUES (%s, %s, %s, %s, %s)""",
			(
				match.duration,
				match.get_score(),
				match.player.id,
				match.category.id,
				match.difficulty.name
			)
		)

	def load_players(self):
		players = self.__select(
			"SELECT name, id FROM players"
		)

		# return players from DB
		return [Player(p[0], p[1]) for p in players]