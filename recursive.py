import numpy as np
import operator as op
from functools import reduce
# import pygraphviz as pgv
from prettytable import PrettyTable

# CHANGE VARIABLES HERE
SURVEY_POP = 10
repeats = 5


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
    P_Y: probability of market share y occuring, our A/(A+B)
    intersections: our A, B, C ... values aka our P(X, Y)'s
    '''

    intersections = []
    for i in range(SURVEY_POP + 1):
        for j in range(len(P_Y)):
            # calculating P(X=i| Y=j) using binominal distribution
            P_XgY = binomial(SURVEY_POP, i, Y[j])

            # calculating P(X, Y) using P(X=i| Y=j)*P(Y[j])
            P_XY = P_XgY * P_Y[j]
            P_XY = round(P_XY, 5)  # rounding to 5 decimal places

            # print(P_XgY, P_Y[j], P_XY)
            intersections.append(P_XY)

    return intersections


def prior(intersections):
    '''
    calculates prior/posterior distribution, A/(A+B)
    ex. for 2 market shares
    A_B = A + B
    return [A / A_B, B / A_B]
    '''

    total = sum(intersections)

    # so sometimes, if the population size is big enough
    # the probabilities of the market share is so low it gets rounded to 0
    # which means total = 0, and our division later throws an error
    # so returning an empty list into our recursive function to let it know
    # this path is done for
    if total == 0:
        return []

    priors = []
    for i in range(len(intersections)):
        prior = round(intersections[i] / total, 5)
        priors.append(prior)

    return priors


def bayesian_table(intersections, repeats, prev_node, count):
    '''
    recursive function to calculate survey results in iterations

    intersections: list of intersection values P(X, Y)s
    repeats: number of repeats
    prev_node: previous node name, used for record keeping
    count: survey 1, used for record keeping
    '''

    # stopping condition, currently just counting repeats
    if (repeats == 0):
        return ""

    for i in range(SURVEY_POP + 1):
        j = i * len(Y)  # getting our index for intersections
        local_intersections = []
        for k in range(j, j + len(Y)):
            local_intersections.append(intersections[k])

        P_Y = prior(local_intersections)  # new P(Y| various X's)
        # if our list is empty, it means prior probability is so unprobable
        # we should probably stop looking down this route
        if len(P_Y) == 0:
            return ''

        cur_x = "X" + str(count) + "=" + str(i) + ', \n' + prev_node
        cur_survey = 'S' + str(count + 1) + ": " + cur_x

        # making a pretty table
        pretty_table = PrettyTable()
        pretty_table.field_names = Y
        pretty_table.add_row(P_Y)

        print('prior probabilities for', cur_x, pretty_table)
        # print(pretty_table)

        intersections2 = get_intersections(Y, P_Y)  # getting new intersection for next survey

        '''
        # drawing nodes in graph
        cur_x = "X" + str(count) + "=" + str(i) + ' P(X)=' + str(A_B) + ', \n' + prev_node
        A = intersections[j]
        B = intersections[j + 1]
        A_B = round(A + B, 4)
        G.add_edge(prev_node, cur_x)
        G.add_edge(cur_x, cur_survey)
        '''

        bayesian_table(intersections2, repeats - 1, cur_survey, count + 1)


if __name__ == "__main__":

    # getting started
    intersections = get_intersections(Y, P_Y)  # our A, B, C, D, ... aka our P(X, Y)'s

    # G.add_edge('start', 'S1')

    # recursion!
    bayesian_table(intersections, repeats, 'S1', 1)

    # G.layout(prog='dot')  # use dot
    # G.draw('graph.png')  # write previously positioned graph to PNG file
