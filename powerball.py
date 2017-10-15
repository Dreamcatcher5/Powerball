"""Author: Ben Johnstone"""

import argparse
import re
from datetime import datetime

import xlrd

from drawing import Drawing

MAX_WHITE = 69
MAX_RED = 26

#TODO
# 1 Do argparse for main
# 3 Figure out what statistics should be reported
# 4 set up logger
# 5 winnings calculator???
# 6 Speed benchmarking??
# 7 Get drawings file from internet
# 8 Graph count of each ball
# Database

def ParseDrawingsFile(fileName):
    """
    This function reads the input file and returns a list of drawings

    """
    drawings = []
    f = open(fileName)
    for line in f:
        lsplit = line.split()
        drawings.append(Drawing(datetime.strptime(lsplit[0], "%m/%d/%Y"), lsplit[1:6], lsplit[6]))
    f.close()
    return drawings

def ParseJackpotFile(fileName):

    jackpots = []
    book = xlrd.open_workbook(fileName)
    jSheet = book.sheet_by_index(0)
    for n in range(jSheet.nrows):
        r = jSheet.row(n)
        #print(r)
        #print(r[0].value)
        try:
            drawingDate = xlrd.xldate.xldate_as_datetime(r[0].value, book.datemode)
            amount = r[2].value
            winnersCol = r[3].value
            winners = re.match("\d+", winnersCol)
            if winners is not None:
                jackpots.append((Drawing(drawingDate, jackpot=amount), winners.group(0)))
        except TypeError:
            pass
    return jackpots

#def WhiteCount(drawings):


#def RedCount(drawings):

def LeastRecentWhites(drawings):
    """Take the list of drawings and return a list of the seen white balls, ordered from least to
    most recent"""

    seenBalls = {}

    # Sort the drawings so we can stop iterating early
    sortedDrawings = sorted(drawings, key=lambda d: d.GetDate(), reverse=True)
    for d in sortedDrawings:
        for b in d.GetNumbers():
            if b not in seenBalls:
                seenBalls[b] = d.GetDate()
        # If we've seen all the balls then we don't need to look anymore
        if len(seenBalls) == MAX_WHITE:
            break

    return [k for k in sorted(seenBalls, key=seenBalls.get)]

def LeastRecentReds(drawings):
    """Take the list of drawings and return a list of the seen red balls, ordered from least to
    most recent"""

    seenBalls = {}

    # Sort the drawings so we can stop iterating early
    sortedDrawings = sorted(drawings, key=lambda d: d.GetDate(), reverse=True)
    for d in sortedDrawings:
        if d.GetPowerball() not in seenBalls:
            seenBalls[d.GetPowerball()] = d.GetDate()
        # If we've seen all the balls then we don't need to look anymore
        if len(seenBalls) == MAX_RED:
            break

    return [k for k in sorted(seenBalls, key=seenBalls.get)]

def MostCommonWhites(drawings):
    """Using a list of drawings, return a list of the white balls, from most to least common"""
    ballCount = dict((k, 0) for k in range(1, MAX_WHITE+1))
    for d in drawings:
        for b in d.GetNumbers():
            ballCount[b] += 1

    return [k for k in sorted(ballCount, key=ballCount.get, reverse=True)]

def MostCommonReds(drawings):
    """Using a list of drawings, return a list of the white balls, from most to least common"""
    ballCount = dict((k, 0) for k in range(1, MAX_RED+1))

    for d in drawings:
        # The number of possible red balls has changed over time. If the ball is not in the current
        # range, ignore it.
        if d in ballCount:
            ballCount[d.GetPowerball()] += 1

    return [k for k in sorted(ballCount, key=ballCount.get, reverse=True)]

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
