#!/usr/bin/env python

from astarnode import AstarNode
from node import Node

if __name__ == '__main__':

    goal = Node('123804765')
    
    initial = AstarNode('217860345',goal=goal)
    #ginitial = AstarNode('123804765', goal=goal)
    opened = [initial]
    closed = []
    counter = 0
    print 'Initial: {0}'.format(initial.to_string())
    print 'Goal   : {0}'.format(goal.to_string())
    raw_input('Continue...')

    while opened != set():
        counter += 1
        print 'Counter: {counter} - Opened: {o} - Closed: {c}'.format(counter=counter, \
                o=len(opened), c=len(closed))
        #order opened
        opened.sort(key=lambda(node): node.f())
        node_to_expand = opened.pop(0)
        closed.append(node_to_expand)

        if node_to_expand == goal:
            print 'goal'
            break;

        succs = node_to_expand.expand()
        for qone in succs:
            if qone not in opened and qone not in closed:
                print 'insert because succ node no esta en las listas'
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


