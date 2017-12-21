"""Play powerball using a series of number picking algorithms and compare the results against
historical powerball drawings

Author: Ben Johnstone

TODO: Start and end dates
"""

import argparse
from json import JSONDecodeError

from picker.factory import PickerFactory
from utilities.fileParser import ParseJSONFile, ParseDrawingsFile, ParseJackpotFile
from utilities.metrics import MostCommonWhites, LeastRecentWhites, MostCommonReds, LeastRecentReds 

class Playmaker(object):

    def __init__(self):
        self._historyFile = ""
        self._jackpotFile = ""
        self._dateStart = None
        self._dateEnd = None
        self._pickCost = 2
        self._outFile = None  ##TODO temporary placeholder, use logger

    # def CalculateWinnings(self, draw, picks):
    #     """Prints the comparison of picks versus a drawing and calculates win amount. TODO Use logger"""
    #     return 1


    def DisplayTotals(self, picks, history):


        # Average whites per pick
        # Average reds per pick
        # Number of winners
        # Number of jackpots
        # Gross winnings
        # Total cost
        # Net winnings

        # placeholder for more complete statistics, just print the total money won
        for k, v in picks.items():
            cost = self._pickCost * k._picksPerDrawing * len(history)
            print("Picker ", k)
            print("\tGross winnings: ", v)
            print("\tTotal cost: ",cost)
            print("\tNet winnings: ", v - cost)
        

    def GetHistoryFile(self):
        return self._historyFile

    def SetConfiguration(self, jsonConfig=None, args=None):
        """Sets the configuration for the run. Values in args will override any values in the
        jsonConfig dictionary

        :param jsonConfig:
        :type jsonConfig:
        :param args:
        :type args:
        :return: 
        """

        for k, v in jsonConfig.items():
            if hasattr(self, "_" + k):
                setattr(self, "_"+ k, v)

        # Let command line args override JSON config

    def Run(self, config, history):
        """Creates pickers from the JSON configuration. Compares picks against historical data
        :param config: Parsed JSON configuration file
        :type config: list
        :param history: Historical drawings
        """
        
        pickers = {}
        #TODO figure out how to do date ranges

        # Create the pickers
        pf = PickerFactory()
        for pickerDict in config["picks"]:
            pickerObj = pf.CreatePicker(pickerDict["name"], **pickerDict)
            if pickerObj is None:
                print("Unable to create picker ", pickerDict["name"])
                continue
            pickers[pickerObj] = 0
        
        # Ignoring start and end date for now
        for i in range(1, len(history)):
            past = history[:i]
            #print(history[i])
            # Make picks based on the previous drawings
            for p, n in pickers.items():
                p.Pick(past)
                for d in p.GetPicks():
                    pickers[p] += history[i].WinAmount(d)

        self.DisplayTotals(pickers, history)



def Main():
    """Reads user input from drawings file and picker JSON. Uses pickers to make picks based on the
    JSON, and will compare them against the historical drawings to calculate winnings."""

    config = ""
    history = []
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--history", required=False,
                        help="Name of the file containing the historical powerball drawings")
    parser.add_argument("--config", "-c", help="JSON configuration file that contains the types" \
                        + " of picks to make", required=True)
    # Start date (optional)
    # End date (optional)
    # Output file
    args = parser.parse_args()
    pm = Playmaker()
    
    try:
        # Parse config file
        jsonConfig = ParseJSONFile(args.config)
        pm.SetConfiguration(jsonConfig=jsonConfig)

        # Parse history file
        history = ParseDrawingsFile(pm.GetHistoryFile())

        pm.Run(jsonConfig, history)

    except JSONDecodeError as e:
        print("JSON error: ", e)


if __name__ == "__main__":
    Main()