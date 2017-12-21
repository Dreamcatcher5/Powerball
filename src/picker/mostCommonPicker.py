"""
A picker for choosing numbers based on the most commonly seen numbers.

Author: Ben Johnstone
"""
import itertools
import random

from drawing import Drawing
from utilities.metrics import MostCommonReds, MostCommonWhites
from picker import Picker
from powerball import NUM_WHITES


class MostCommonPicker(Picker):

    def __init__(self, **kwargs):
        super(MostCommonPicker, self).__init__(**kwargs)

    def Pick(self, pastDrawings):
        """Make drawings based on the most common numbers.
        :param pastDrawings:    Previous drawings that can be used to base picks on
        :type pastDrawings:     list of Drawings
        :return:                list of Drawings created by the picker"""
        
        self._picks = []
        mcReds = MostCommonReds(pastDrawings)
        mcWhites = MostCommonWhites(pastDrawings)

        # Pick white balls using permutations of the least recent balls
        permIter = itertools.permutations(mcWhites, r=NUM_WHITES)
        for i in range(self._picksPerDrawing):
            redPick = mcReds[0] if not self._altReds else random.choice(mcReds[:NUM_WHITES])
            self._picks.append(Drawing(None, numbers=next(permIter), powerball=redPick))

        return self._picks
