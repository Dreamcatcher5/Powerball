"""
A picker for choosing numbers based on what has been seen least recently.

Author: Ben Johnstone
"""
import itertools
import random

from drawing import Drawing
from utilities.metrics import LeastRecentReds, LeastRecentWhites
from picker import Picker
from powerball import NUM_WHITES

class LeastRecentPicker(Picker):

    def __init__(self, **kwargs):
        super(LeastRecentPicker, self).__init__(**kwargs)

    def Pick(self, pastDrawings):
        """Make drawings based on the least recent numbers.
        :param pastDrawings:    Previous drawings that can be used to base picks on
        :type pastDrawings:     list of Drawings
        :return:                list of Drawings created by the picker"""
        
        self._picks = []
        lrReds = LeastRecentReds(pastDrawings)
        lrWhites = LeastRecentWhites(pastDrawings)

        # Pick white balls using permutations of the least recent balls
        permIter = itertools.permutations(lrWhites, r=NUM_WHITES)
        for i in range(self._picksPerDrawing):
            redPick = lrReds[0] if not self._altReds else random.choice(lrReds[:NUM_WHITES])
            self._picks.append(Drawing(None, numbers=next(permIter), powerball=redPick))

        return self._picks
