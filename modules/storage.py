import abc
import mysql.connector
from trivia import Player, Category, PlayerStatistics

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

	@abc.abstractmethod
	def load_categories(self):
		pass

	@abc.abstractmethod
	def load_player_statistics(self, player):
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
		if match == None or match.player == None:
			return False

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
			"""SELECT
				p.id,
				p.`name`,
				SUM(m.score) AS tscore
			FROM players p
			LEFT JOIN matches m ON m.id_player = p.id
			GROUP BY p.id
			ORDER BY tscore DESC"""
		)

		# return players from DB ranked by the best
		return [Player(p[1], p[0]) for p in players]

	def load_categories(self):
		categories = self.__select(
			"SELECT `name`, id FROM categories"
		)

		# return categories from DB
		return [Category(c[0], c[1]) for c in categories]

	def load_player_statistics(self, player):
		if player == None:
			return None
		
		s = PlayerStatistics()

		# check if has statistics
		s.games_played			= self.__select("SELECT COUNT(*) FROM matches WHERE id_player = %s", (player.id,), True)
		if s.games_played == None or s.games_played[0] == 0:
			return None

		s.games_played = s.games_played[0]
		s.wins					= self.__select("SELECT COUNT(*) FROM matches WHERE id_player = %s AND score >= 7", (player.id,), True)[0]
		s.time_played			= self.__select("SELECT SUM(duration) FROM matches WHERE id_player = %s", (player.id,), True)[0]
		s.best_categories		= self.__select(
			"""
			SELECT
				cat.id,
				cat.`name`,
				SUM(score) AS tscore
			FROM matches m
			INNER JOIN categories cat ON m.id_category = cat.id AND id_player = %s
			GROUP BY id_category
			ORDER BY tscore DESC
			""",
			(player.id,)
		)

		# get ranking
		ranking	= self.__select(
			"""
			SELECT p.id FROM players p
			INNER JOIN matches m ON p.id = m.id_player
			GROUP BY p.id
			ORDER BY SUM(m.score) DESC
			"""
		)

		ra = 1 # get player ranking
		for r in ranking:
			if r[0] == player.id:
				s.ranking = ra
				break
			
			ra += 1

		# convert categories data into Category objects
		s.best_categories = [Category(c[1], c[0]) for c in s.best_categories]

		return s