#!/usr/bin/env python

from puzzle8 import Node
from time import time

if __name__ == '__main__':

    goal = Node('123804765')
    #TODO: Check parity errors
    initial = Node('127860345')
    opened = set([initial])
    closed = set()
    counter = 0
    result = 'Goal not found'

    print 'Initial: {0}'.format(initial.to_string())
    print 'Goal   : {0}'.format(goal.to_string())
    raw_input('Continue...')
    time_init = time()

    while opened != set():
        counter += 1
        print 'Counter: {0} - Open Nodes: {1}'.format(counter, len(opened))
        node_to_expand = opened.pop()
        closed.add(node_to_expand)
        succ = []
        if node_to_expand.matrix == goal.matrix:
            time_end = time()
            result = 'Goal found in {0:.2f} seconds'.format(time_end - time_init)
            break;
        up, down, left, right = node_to_expand.expand()
        if up not in closed:
            opened.add(up)
        if down not in closed:
            opened.add(down)
        if left not in closed:
            opened.add(left)
        if right not in closed:
            opened.add(right)

    print result
