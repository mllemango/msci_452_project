import numpy as np
import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom


if __name__ == "__main__":

    survey_pop = 2
    Y = 0.5
    P_YgX0 = [0.5, 0.5]
    P_YgX1 = [0.5, 0.5]
    P_YgX2 = [0.5, 0.5]

    givens = {0: P_YgX0, 1: P_YgX1, 2: P_YgX2}
    ands = {0: [], 1: [], 2: []}
    ands2 = {0: [], 1: [], 2: []}
    survey1 = []
    i, j = 0, 0
    for i in range(survey_pop + 1):

        # is it accurate
        '''
        X = probability of current branch happening
        Y1 = probability of market share greater than y%, 0.5
        Y2 = probability of market share less than y%, 0.5

        variables
        probability of X = Binomial
        probability of Y and X = algebra
        probability of Y given X = known value
        '''

        P_X = ncr(survey_pop, i) * (Y) ** survey_pop
        # print(P_X)

        P_XY1 = givens[i][0] * P_X
        P_XY2 = givens[i][1] * P_X

        list = [P_XY1, P_XY2]
        ands[i] = list

        for j in range(survey_pop + 1):
            P_X2 = ncr(survey_pop, j) * (Y) ** survey_pop

            ands2[i].append(givens[i][0] * P_X2)
            ands2[i].append(givens[i][1] * P_X2)

    print(ands)
    print(ands2)
