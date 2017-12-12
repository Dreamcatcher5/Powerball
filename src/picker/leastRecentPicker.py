"""
A picker for choosing numbers based on what has been seen least recently.

Author: Ben Johnstone
"""
from utilities.metrics import LeastRecentReds, LeastRecentWhites
from picker import Picker

class LeastRecentPicker(Picker):

    def __init__(self, **kwargs):
        super(RandomPicker, self).__init__(**kwargs)

    def Pick(self, pastDrawings):
        """Make drawings by picking numbers randomly.
        :param pastDrawings:    Previous drawings that can be used to base picks on
        :type pastDrawings:     list of Drawings
        :return:                list of Drawings created by the picker"""
        return None
        #lrReds = LeastRecentReds(pastDrawings)
        #lrWhites = LeastRecentWhites(pastDrawings)


