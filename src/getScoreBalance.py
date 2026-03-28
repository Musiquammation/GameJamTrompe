from math import log

def getScoreBalance(x: float):
    return 6 / (log(100 * max(100, x - 500)) + 1)