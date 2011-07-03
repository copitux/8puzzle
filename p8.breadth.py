#!/usr/bin/env python

from node import Node
from time import time

if __name__ == '__main__':

    goal = Node('123804765')
    initial = Node('217860345')
    opened = set([initial])
    closed = set()
    counter = 0
    result = 'Goal not found'

    print 'Initial: {0}'.format(initial.to_string())
    print 'Goal   : {0}'.format(goal.to_string())
    if initial.parity_error(goal):
        print 'Parity error: have not solution' 
        
    raw_input('Continue...')
    time_init = time()

    while opened != set():
        counter += 1
        print 'Counter: {0} - Open Nodes: {1}'.format(counter, len(opened))
        node_to_expand = opened.pop()
        closed.add(node_to_expand)
        succ = []
        if node_to_expand == goal:
            time_end = time()
            result = 'Goal found in {0:.2f} seconds. Depth: {1}'.format(
                    time_end - time_init, node_to_expand.depth)
            break;
        succs = node_to_expand.expand()
        for node in succs:
            if node not in closed:
                opened.add(node)

    print result
