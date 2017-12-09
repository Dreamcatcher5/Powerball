

class Picker(object):

    def __init__(self, **kwargs):
        self._picks = []



    def GetPicks(self):

        return self._picks


    # set alternate reds

    # get/set num picks per drawing

    # abstract method decorator here
    def Pick(self, pastDrawings, numPicks, altReds=True):
        return self._picks