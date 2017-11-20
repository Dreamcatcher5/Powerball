"""Play powerball using a serices of number picking algorithms and compare the results against
historical powerball drawings

Author: Ben Johnstone

TODO: Start and end dates
"""

from utilities.fileParser import ParseJSONFile, ParseDrawingsFile, ParseJackpotFile



def SetConfiguration(config, jsonConfig, args):
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

def Run(config, history):
	"""Creates pickers from the JSON configuration. Compares picks against historical data
	:param config: Parsed JSON configuration file
	:type config: list
	:param history: Historical drawings
	"""



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

    # Parse config file
    with open(args.config) as f:
    	config = f.read()

    json_config = json.loads(config)

    # Parse history file
    history = ParseDrawingsFile(args.history)
    # validate against start/end dates

    Run(json_config, args.history)


if __name__ == "__main__":
	Main()