"""Play powerball using a serices of number picking algorithms and compare the results against
historical powerball drawings

Author: Ben Johnstone

TODO: Start and end dates
"""

from picker.factory import PickerFactory
from utilities.fileParser import ParseJSONFile, ParseDrawingsFile, ParseJackpotFile


class Playmaker(object):

    def __init__(self):
        self._historyFile = ""
        self._jackpotFile = ""
        self._dateStart = None
        self._dateEnd = None
        self._pickCost = 2
        self._outFile = None  ##TODO temporary placeholder, use logger

    def CalculateWinnings(self, draw, picks):
        """Prints the comparison of picks versus a drawing and calculates win amount. TODO Use logger"""
        


    def DisplayTotals(self, picks):


        # Average whites per pick
        # Average reds per pick
        # Number of winners
        # Number of jackpots
        # Gross winnings
        # Total cost
        # Net winnings

        # placeholder for more complete statistics, just print the total money won


    def SetConfiguration(self, config=None, jsonConfig=None, args=None):
        """Sets the configuration for the run. Values in args will override any values in the
        jsonConfig dictionary

        :param config:
        :type config:
        :param jsonConfig:
        :type jsonConfig:
        :param args:
        :type args:
        :return: 
        """

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
            pickerObj = pf.CreatePicker(pickerDict["name"], pickerDict)
            if pickerObj is None:
                print("Unable to create picker ", pickerDict["name"])
                continue
            pickers[pickerObj] = 0
        # Ignoring start and end date for now

        for i in range(1, len(history)):
            past = history[:i]

            # Make picks based on the previous drawings
            for p, n in pickers.items():
                p.Pick(past)
                pickers[p] += CalculateWinnings(past, p)

        DisplayTotals(picks)



def Main():
	"""Reads user input from drawings file and picker JSON. Uses pickers to make picks based on the
	JSON, and will compare them against the historical drawings to calculate winnings."""

	config = ""
	history = []
	parser = argparse.ArgumentParser(description="")
    parser.add_argument("--history", "-h", required=False,
                        help="Name of the file containing the historical powerball drawings")
    parser.add_argument("--config", "-c", help="JSON configuration file that contains the types" \
        	            + " of picks to make", required=False)
    # Start date (optional)
    # End date (optional)
    # Output file
    args = parse.parse_args()
    pm = Playmaker()

    try:
        # Parse config file
        json_config = ParseJSONFile(args.config)
        pm.SetConfiguration(json_config=json_config)

        # Parse history file
        history = ParseDrawingsFile(args.history)
        # validate against start/end dates

    except JsonException as e:
        print("JSON error")
        print(e)
    except Exception as e:
        print(e)

    #Run(json_config, args.history)


if __name__ == "__main__":
	Main()