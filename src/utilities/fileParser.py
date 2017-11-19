

import argparse
import re
from datetime import datetime

import xlrd

from drawing import Drawing



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