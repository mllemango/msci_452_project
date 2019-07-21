import numpy as np
import operator as op
from functools import reduce

'''
function to perform nCr
'''
def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom


if __name__ == "__main__":

    Y1 = 0.1  # market share
    Y2 = 0.2  # market share

    P_Y1 = 0.8  # probability of market share = 0.1
    P_Y2 = 0.2  # probability of market share = 0.2

    # P(Y1|X)'s, known values set here
    # P(Y2|X)'s, known values set here
    P_Y1gX = []
    P_Y2gX = []
    survey_pop = 2  # number of participants/ survey population
    for i in range(0, survey_pop):
        P_Y1gX.append(0.5)
        P_Y2gX.append(0.5)

    # P(Y, X), to be set
    ands = {0: [], 1: [], 2: []}
    ands2 = {0: [], 1: [], 2: []}

    for i in range(0, survey_pop + 1):

        # finding P(X=i|Y1)
        P_XgY1 = ncr(survey_pop, i) * ((Y1) ** (i)) * ((1 - Y1) ** (survey_pop - i))
        # finding P(X=i|Y2)
        P_XgY2 = ncr(survey_pop, i) * ((Y2) ** (i)) * ((1 - Y2) ** (survey_pop - i))

        # Finding P(X, Y1), P(X, Y2)
        P_XY1 = P_XgY1 * P_Y1
        P_XY2 = P_XgY2 * P_Y2

        list = [P_XY1, P_XY2]
        ands[i] = list

    print(ands)
    # print(ands2)
