


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