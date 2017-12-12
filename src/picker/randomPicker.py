"""
A picker for choosing numbers randomly

Author: Ben Johnstone
"""
import random

from drawing import Drawing
from picker import Picker
from powerball import MAX_RED, MAX_WHITE

class RandomPicker(Picker):

    def __init__(self, **kwargs):
        super(RandomPicker, self).__init__(**kwargs)

    def Pick(self, pastDrawings):
        """Pick numbers randomly and put them into drawings"""
        randRed = None
        self._picks = []
        for _ in range(self._picksPerDrawing):
            reds = random.sample(range(MAX_WHITE+1), 5)
            if self._altReds or randRed is None:
                randRed = random.randint(0, MAX_RED)
            draw = Drawing(None, reds, randRed)
            self._picks.append(draw)
        return self._picks
