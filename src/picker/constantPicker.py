"""
A picker for choosing the same numbers each time.

Author: Ben Johnstone
"""

from drawing import Drawing
from picker import Picker

class ConstantPicker(Picker):

    def __init__(self, **kwargs):
        super(ConstantPicker, self).__init__(**kwargs)

    def SetPicks(self, picks):
        self._picks = picks

    def Pick(pastDrawings):
        """Always return the same picks"""
        return self._picks