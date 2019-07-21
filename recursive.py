import numpy as np
import operator as op
from functools import reduce


def ncr(n, r):
    '''
    performs n choose r
    '''
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer / denom


def binomial(n, r, P):
    '''
    binomial distribution formula
    '''
    return ncr(n, r) * ((P) ** (r)) * ((1 - P) ** (n - r))


def get_intersections(Y, P_Y):
    '''
    Y: market share variables
    P_Y: probability of market share y occuring
    intersections: our A, B, C ... values aka our P(X, Y)'s
    '''
    SURVEY_POP = len(Y)

    intersections = []
    for i in range(SURVEY_POP + 1):
        for j in range(len(Y)):
            # calculating P(X=i| Y=j) using binominal distribution
            P_XgY = binomial(SURVEY_POP, i, Y[j])

            # calculating P(X, Y) using P(X=i| Y=j)*P(Y[j])
            P_XY = P_XgY * P_Y[j]

            # print(P_XgY, P_Y[j], P_XY)
            intersections.append(P_XY)
    return intersections


def bayesian_table(intersections):
    '''
    recursive function to calculate survey in iterations
    '''
    SURVEY_POP = len(intersections) / 2
    for i in range(SURVEY_POP):
        count = i * 2  # getting our index for intersections
        intersections2 = get_intersections(intersections[count], intersections[count + 1])


if __name__ == "__main__":
    # setting market share variables
    Y1 = 0.1  # market share 1
    Y2 = 0.2  # market share 2
    Y = [Y1, Y2]

    P_Y1 = 0.8  # probability of market share = 0.1
    P_Y2 = 0.2  # probability of market share = 0.2
    P_Y = [P_Y1, P_Y2]

    intersections = []  # our A, B, C, D, ... aka our P(X, Y)'s
    intersections = get_intersections(Y, P_Y)

    print(intersections)
