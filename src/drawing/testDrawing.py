from datetime import date
from drawing import Drawing


# Test comparing two picks
theDrawing = Drawing(date.today(), numbers=[1,2,3,4,5], powerball=1)
print(theDrawing)

#
pick1 = Drawing(None, numbers=[1,2,3,4,5], powerball=1)
print(theDrawing.MatchingNumbers(pick1))
print(theDrawing.MatchingPowerball(pick1))
print(theDrawing.IsJackpot(pick1))
print(theDrawing.WinAmount(pick1))





