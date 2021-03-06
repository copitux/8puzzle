#!/usr/bin/env python

from astarnode import AstarNode
from node import Node
from time import time

if __name__ == '__main__':

    goal = Node('123804765')
    
    initial = AstarNode('127860345',goal=goal)
    opened = [initial]
    closed = []
    counter = 0
    print 'Initial: {0}'.format(initial.to_string())
    print 'Goal   : {0}'.format(goal.to_string())
    if initial.parity_error():
        print 'Parity error: have not solution' 

    raw_input('Continue...')
    time_init = time()

    while opened != set():
        counter += 1
        print 'Counter: {counter} - Opened: {o} - Closed: {c}'.format(counter=counter, \
                o=len(opened), c=len(closed))
        opened.sort(key=lambda(node): node.f())
        node_to_expand = opened.pop(0)
        closed.append(node_to_expand)

        if node_to_expand == goal:
            print 'Goal found in {0:.2f} seconds in depth {1}'.format(time() - time_init, \
            node_to_expand.depth)
            break;

        succs = node_to_expand.expand()
        for qone in succs:
            if qone not in opened and qone not in closed:
                opened.append(qone)
            else:
                flag_opened = True
                try:
                    qzero_index = opened.index(qone)
                    qzero = opened[qzero_index]
                except ValueError:
                    qzero_index = closed.index(qone)
                    qzero = closed[qzero_index]
                    flag_opened = False

                if qzero.g > qone.g:
                    if flag_opened:
                        opened.pop(qzero_index)
                    else:
                        closed.pop(qzero_index)
                    opened.append(qone)

