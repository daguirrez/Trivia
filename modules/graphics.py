import abc

class IScreen(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def draw(self):
		pass