#!/usr/bin/env python
from random import randint

class Node(object):
    """
    Node object implemented with strings

    string: '012345678' is in bidimensional matrix mode:

        | 0 | 1 | 2 |
        | 3 | 4 | 5 |
        | 6 | 7 | 8 |

    """
    def __init__(self, matrix=None):
        if not matrix:
            self.matrix = self.shuffle('012345678')
        else:
            self.matrix = map(int,list(matrix))

    def __str__(self):
        to_print = ''
        for i in range(len(self.matrix)):
            to_print += '{0:^3}|'.format(self.matrix[i])
            if i == 2 or i == 5:
                to_print += '\n'
        return to_print

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.matrix == other.matrix

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        """ To check in set.add """
        return int(self.to_string())

    def shuffle(self, matrix):
        matrix = list(matrix)
        randmatrix = []
        for i in range(len(matrix)):
            index = randint(0, len(matrix)-1)
            randmatrix.append(int(matrix.pop(index)))
        return randmatrix

    def zero_index(self):
        return self.matrix.index(0)
    
    def expand(self):
        """ 
        Order import 

        TODO: not DRY!, maybe copy learn
        """
        initial_string = self.to_string()
        node_up = Node(initial_string)
        node_down = Node(initial_string)
        node_left = Node(initial_string)
        node_right = Node(initial_string)
        return node_up.up(), node_down.down(), node_left.left(), node_right.right()

    def up(self):
        z = self.zero_index()
        if z > 2:
            self.matrix[z], self.matrix[z-3] = self.matrix[z-3], self.matrix[z]
        return self

    def down(self):
        z = self.zero_index()
        if z < 6:
            self.matrix[z], self.matrix[z+3] = self.matrix[z+3], self.matrix[z]
        return self

    def left(self):
        z = self.zero_index()
        if z not in [0,3,6]:
            self.matrix[z], self.matrix[z-1] = self.matrix[z-1], self.matrix[z]
        return self

    def right(self):
        z = self.zero_index()
        if z not in [2,5,8]:
            self.matrix[z], self.matrix[z+1] = self.matrix[z+1], self.matrix[z]
        return self

    def to_string(self):
        return ''.join(map(str, self.matrix))
