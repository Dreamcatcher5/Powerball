

class Picker(object):

    def __init__(self, picksPerDrawing=1, altReds=True, **kwargs):
        self._picks = []
        self._picksPerDrawing = picksPerDrawing
        self._altReds = altReds




    def GetPicks(self):

        return self._picks


    # set alternate reds

    # get/set num picks per drawing

    # abstract method decorator here
    def Pick(self, pastDrawings):
        return self._picks