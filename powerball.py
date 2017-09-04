"""Author: Ben Johnstone"""

import argparse
from datetime import datetime

from drawing import Drawing

#TODO
# 1 Do argparse for main
# 2 Write drawing class
# 3 Figure out what statistics should be reported
# 4 set up logger

def ParseDrawingsFile():
    """
    This function reads the input file and returns a list of drawings

    """
    drawings = []
    f = open("powerball.txt")
    for line in f:
        print(line)
        lsplit = line.split()
        drawings.append(Drawing(lsplit[0], set(lsplit[1:6]), lsplit[6])
    f.close()
    return drawings

def PrintStats(whiteList, redList):
    # Compile everything, print results
    for i in range(60,70):
        whiteList[i] *= 63.3
    white_sorted = sorted(whiteList.keys(), reverse=True)
    #white_sorted.sort(cmp=lambda x,y: cmp(whiteList[x], whiteList[y]))
    print()
    print("White Balls:")
    for i in white_sorted:
        print("Ball %d: %f" % (i, whiteList[i]*100/wc))
        
    white_sorted = sorted(lrp.keys(), reverse=True)
    #white_sorted.sort(cmp=lambda x,y: -1*cmp(lrp[x], lrp[y]))
    print()
    print("Least Recent White Balls:")
    for i in white_sorted:
        print("Ball %d: %f" % (i, lrp[i]))

    #Red balls
    red_sorted = sorted(redList.keys(), reverse=True)
    #red_sorted.sort(cmp=lambda x,y: -cmp(redList[x], redList[y]))
    red_sorted
    print()
    print("Red Balls:")
    for i in red_sorted:
        print("Ball %d: %f" % (i, redList[i]*100/rc))
        

    red_sorted = lrpr.keys()
    red_sorted.sort(cmp=lambda x,y: -1*cmp(lrpr[x], lrpr[y]))
    print()
    print("Least Recent Red Balls:")
    for i in red_sorted:
        print ("Ball %d: %f" % (i, lrpr[i]))


def Main():

    drawings = []
    whiteList, redList = ParseDrawingsFile()
    PrintStats(whiteList, redList)

if __name__ == "__main__":
    Main()
