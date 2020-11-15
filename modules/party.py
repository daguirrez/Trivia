import abc

class IParty(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def get_match(self):
		pass