import Picker
import Powerball

class LeastRecentPicker(Picker):

    def __init__(self):
        super(RandomPicker, self).__init__()

    def Pick(pastDrawings, numPicks, altWhites=True):

        lrReds = leastRecentReds(pastDrawings)
        lrWhites = leastRecentWhites(pastDrawings)


