
from datetime import datetime

from powerball import NUM_WHITES
class Drawing():

	JACKPOT = -1

	def __init__(self, date, numbers=[], powerball=0, jackpot=None):
		self._date = date
		self._numbers = set(int(n) for n in list(numbers))
		self._powerball = int(powerball)
		self._jackpot = self.JACKPOT if jackpot is None else jackpot

	def __repr__(self):

		strRep = ""
		if self._date is not None:
			strRep = "Drawing date: " +  self._date.strftime("%A %m/%d/%Y") + "\n"
		return strRep + "Numbers: [" + " ".join([str(x) for x in self._numbers]) + \
					"]\tPowerball: " + str(self._powerball)


	def GetDate(self):
		return self._date

	def GetNumbers(self):
		return self._numbers

	def GetPowerball(self):
		return self._powerball

	def MatchingNumbers(self, picks):
		"""Determine how many of the pick's numbers match the Drawing's numbers"""
		return len(picks.GetNumbers() & self._numbers)

	def MatchingPowerball(self, picks):
		return picks.GetPowerball() == self._powerball

	def IsJackpot(self, picks):
		return (self.MatchingNumbers(picks) == NUM_WHITES) and self.MatchingPowerball(picks)

	def WinAmount(self, picks):
		"""Determine winnings based on the picks"""
		amt = 0
		red = self.MatchingPowerball(picks)
		numMatching = self.MatchingNumbers(picks)

		if not red and numMatching < 3:
			amt =  0
		elif red and numMatching == NUM_WHITES:
			amt = JACKPOT
		elif numMatching == NUM_WHITES:
			amt = 1000000
		elif red and numMatching == 4:
			amt = 50000
		elif numMatching == 4 or (red and numMatching == 3):
			amt = 100
		elif (red and numMatching == 2) or numMatching == 3:
			amt = 7
		elif red:
			amt = 4

		return amt