"""
A picker for choosing numbers randomly

"""
import random

from powerball.drawing import Drawing
from picker import Picker
from Powerball import MAX_RED, MAX_WHITE

class RandomPicker(Picker):

    def __init__(self):
        super(RandomPicker, self).__init__()

    def Pick(pastDrawings, numPicks, altWhites=True):
        """Pick numbers randomly and put them into drawings"""
        randWhite = None

        for _ in range(numPicks):
            reds = random.sample(range(MAX_RED+1), 5)
            if altWhites or randWhite is None:
                randWhite = random.randint(0, MAX_WHITE)
            draw = Drawing(None, reds, randWhite)
            self.picks.append(draw)
        return self.picks
