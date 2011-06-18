#!/usr/bin/env python
from random import randint

class Node(object):
    
    def __init__(self, matrix=None):
        if not matrix:
            self.matrix = self.shuffle('012345678')
        else:
            self.matrix = map(int,list(matrix))
        self.zero = self.zero_posit()

    def __repr__(self):
        to_print = ''
        for i in range(len(self.matrix)):
            to_print += '{0:^3}|'.format(self.matrix[i])
            if i == 2 or i == 5:
                to_print += '\n'
        return to_print
    def __str__(self):
        return str(self.__repr__)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.matrix == other.matrix

    def __ne__(self, other):
        return not self.__eq__(other)

    def shuffle(self, matrix):
        matrix = list(matrix)
        randmatrix = []
        for i in range(len(matrix)):
            index = randint(0, len(matrix)-1)
            randmatrix.append(int(matrix.pop(index)))
        return randmatrix

    def zero_posit(self):
        try:
            return self.zero
        except AttributeError as e:
            return self.matrix.index(0)
            
    def up(self):
        z = self.zero_posit()
        if z > 2:
            self.matrix[z], self.matrix[z-3] = self.matrix[z-3], self.matrix[z]
            self.zero = z-3
        else:
            return False

    def down(self):
        z = self.zero_posit()
        if z < 6:
            self.matrix[z], self.matrix[z+3] = self.matrix[z+3], self.matrix[z]
            self.zero = z+3
        else:
            return False

    def left(self):
        z = self.zero_posit()
        if z not in [0,3,6]:
            self.matrix[z], self.matrix[z-1] = self.matrix[z-1], self.matrix[z]
            self.zero = z-1
        else:
            return False

    def right(self):
        z = self.zero_posit()
        if z not in [2,5,8]:
            self.matrix[z], self.matrix[z+1] = self.matrix[z+1], self.matrix[z]
            self.zero = z+1
        else:
            return False

    def to_string(self):
        return ''.join(map(str, self.matrix))
