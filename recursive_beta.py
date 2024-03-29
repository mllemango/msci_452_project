'''
recursive.py with beta function instead
'''

import time
import numpy as np
import operator as op
from functools import reduce
# import pygraphviz as pgv
from prettytable import PrettyTable

# CHANGE VARIABLES HERE
SURVEY_POP = 5
repeats = 2
accept = 0.95


# setting market share variables
Y1 = 0.14  # market share 1
Y2 = 0.15  # market share 2
Y3 = 0.17
Y4 = 0.2
Y = [Y1, Y2, Y3, Y4]

P_Y1 = 0.3333  # probability of market share = 0.14
P_Y2 = 0.1667  # probability of market share = 0.15
P_Y3 = 0.3333
P_Y4 = 0.1667
P_Y = [P_Y1, P_Y2, P_Y3, P_Y4]

# G = pgv.AGraph()
results = open("results.txt", "w")


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


def beta(r, n, P):
    '''
    beta distribution for P<p
    '''
    sum = 0
    for i in range(0, r):
        sum = sum + binomial(n-1, i, P)

    return 1 - sum


def bayesian_table(n, r, repeats, accept, prev_node, count):
    '''
    recursive function to calculate survey results in iterations

    repeats: number of repeats
    accept: the confidence we are ok with terminating the surveys at
    prev_node: previous node name, used for record keeping
    count: survey 1, used for record keeping
    '''

    # stopping condition, currently just counting repeats
    if (repeats == 0):
        return ""
    new_n = n + SURVEY_POP
    for i in range(SURVEY_POP + 1):

        # book keeping
        cur_x = "X" + str(count) + "=" + str(i) + ', \n' + prev_node

        # calculating new beta distr values
        new_r = r + i
        for j in range(len(Y)):
            P = Y[j]
            posterior = beta(new_r, new_n, P)
            print(P, posterior, cur_x)

            # checking for stopping condition
            if posterior >= accept:

                results.write(str(P) + '\n')
                results.write('stopped at ' + str(posterior) + " n: " + str(new_n) + ", r: " + str(new_r) + '\n')
                results.write(cur_x)
                results.write('\n')
                return ''
            bayesian_table(new_n, new_r, repeats - 1, accept, cur_x, count + 1)


if __name__ == "__main__":

    # getting started
    start = time.time()
    results.write("start!\n")
    # G.add_edge('start', 'S1')

    # recursion! starting the recursion with r = 0, r = 1, ... r = 5
    for i in range(SURVEY_POP+1):
        cur_x = 'X1=' + str(i) + '\n'
        bayesian_table(SURVEY_POP, i, repeats, accept, cur_x, 2)

    end = time.time()
    total = str(end - start)
    results.write("recursive.py took " + total + 's')

    # G.layout(prog='dot')  # use dot
    # G.draw('graph.png')  # write previously positioned graph to PNG file
