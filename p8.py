#!/usr/bin/env python

from puzzle8 import Node
from copy import copy

if __name__ == '__main__':

    #bragas
    goal = Node('123804765')
    #goal = Node('123456780')
    #goal = Node()

    #bragas
    initial = Node('217860345')
    #initial = Node('123746058')
    opened = set()
    closed = set()

    # up down left right
    opened.add(initial)
    print 'Initial: {0}'.format(initial.to_string())
    print 'Goal   : {0}'.format(goal.to_string())
    raw_input('continua...')
    i = 1
    while opened != set():
        i += 1
        print 'Iteracion: %d' % i
        node_to_expand = opened.pop()
        closed.add(node_to_expand)
        succ = []
        if node_to_expand.matrix == goal.matrix:
            print 'goal'
            break;
        snode_to_expand = node_to_expand.to_string()
        up = Node(snode_to_expand)
        up.up()
        down = Node(snode_to_expand)
        down.down()
        left = Node(snode_to_expand)
        left.left()
        right = Node(snode_to_expand)
        right.right()
        if up not in closed:
            opened.add(up)
        if down not in closed:
            opened.add(down)
        if left not in closed:
            opened.add(left)
        if right not in closed:
            opened.add(right)
        #import ipdb; ipdb.set_trace()
        print len(opened)
