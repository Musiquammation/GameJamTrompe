from math import log

def getScoreBalance(x: float):
    return 5.605 / (log(100 * max(100, x)) + 1)