"""Author: Ben Johnstone"""
MAX_WHITE = 69
MAX_RED = 26

class Drawing():


	NUM_WHITES = 5

	def __init__(self, date, numbers, powerball):
		self._date = date
		self._numbers = numbers
		self._powerball = powerball

	def GetDate():
		return self._date

	def GetNumbers():
		return self._numbers


	def GetPowerball():
		return self._powerball

	def MatchingNumbers(self, picks):
		"""Determine how many of the pick's numbers match the Drawing's numbers"""
		return len(set(picks.GetNumbers()) & set(self._numbers))

	def MatchingPowerball(self, picks):
		return picks.GetPowerball() == self._powerball

	def IsJackpot(self, picks):
		return (self.MatchingNumbers(picks) == NUM_WHITES) and self.MatchingPowerball(picks)

	def WinAmount(self, picks):
		"""Determine winnings based on the picks"""

		