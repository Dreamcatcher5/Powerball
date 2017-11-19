"""Author: Ben Johnstone"""

#TODO
# 1 Do argparse for main
# 3 Figure out what statistics should be reported
# 4 set up logger
# 5 winnings calculator???
# 6 Speed benchmarking??
# 7 Get drawings file from internet
# 8 Graph count of each ball
# Database

def Main():

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--file", "-f", required=True,
                        help="Name of the file containing the historical powerball drawings")
    parser.add_argument("--jackpot", "-j", help="Optional excel file containing the number of " \
                        + "jackpot winners for each drawing")
    parser.add_argument("--leastRecent", "-l", help="Display the white and red numbers in order " \
                        + "from least to most recently drawn", action="store_true")
    parser.add_argument("--mostCommon", "-m", help="Display the white and red numbers in order " \
                        + "of commonality in the results from most to least common",
                        action="store_true")

    args = parser.parse_args()

    if not (args.leastRecent or args.mostCommon):
        print("Must use at least one of --leastRecent or --mostCommon")
        return

    drawings = ParseDrawingsFile(args.file)

    if args.jackpot:
        ParseJackpotFile(args.jackpot)
    
    if args.leastRecent:
        print("Least recent white balls:")
        print(LeastRecentWhites(drawings))
        print("Least recent red balls:")
        print(LeastRecentReds(drawings))

    if args.mostCommon:
        print("Most common white balls:")
        print(MostCommonWhites(drawings))
        print("Most common red balls:")
        print(MostCommonReds(drawings))

if __name__ == "__main__":
    Main()
