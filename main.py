import numpy as np
import operator as op
from functools import reduce

fair_flips = np.random.binomial(1, 0.5, 2)


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom


survey_pop = 3
for i in range(survey_pop+1):

    # is it accurate
    '''
    X = probability of current branch happening
    Y = probability of market share greater than y%

    variables
    probability of X = Binomial
    probability of Y and X = algebra
    probability of Y given X = known value
    '''

    P_X = ncr(survey_pop, i) * (0.5*0.5*0.5)
    print(P_X)
