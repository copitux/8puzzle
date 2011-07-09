from random import randint

class Node(object):
    """
    Node object implemented with strings

    string: '012345678' is in bidimensional matrix mode:

        | 0 | 1 | 2 |
        | 3 | 4 | 5 |
        | 6 | 7 | 8 |

    """
    def __init__(self, matrix=None, depth=0):
        if not matrix:
            self.matrix = self.shuffle('012345678')
        else:
            self.matrix = map(int,list(matrix))
        self.depth = depth

    def __str__(self):
        to_print = ''
        for i, v in enumerate(self.matrix):
            to_print += '{0:^3}|'.format(v)
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
        
        initial_string = self.to_string()
        depth = self.depth + 1
        node_left = Node(initial_string, depth)
        node_up = Node(initial_string, depth)
        node_right = Node(initial_string, depth)
        node_down = Node(initial_string, depth)
       
	return node_left.left(), node_up.up(), node_right.right(), node_down.down()

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

    def parity_error(self, goal=None):
        try:
            goal = self.goal.matrix
        except AttributeError:
            goal = goal.matrix
        initial = self.matrix

        inversions = 0
        for i in range(1,9):
            slicing_init = set(initial[initial.index(i)+1:])
            slicing_goal = set(goal[0:goal.index(i)])
            inversions += len(slicing_init & slicing_goal)

        return True if (inversions % 2) != 0 else False
