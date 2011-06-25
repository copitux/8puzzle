from node import Node

class AstarNode(Node):

    def __init__(self, matrix=None, goal=None, parent=None, depth=0):
        super(AstarNode, self).__init__(matrix, depth)
        self.goal = goal
        self.parent = parent
        self.g = self.calcg()
    
    def calcg(self):
        if self.parent is None:
            return self.heuristic_desorder()
        else:
            return self.parent.g + self.heuristic_desorder()

    def heuristic_desorder(self):
        goal = self.goal.matrix
        matrix, not_in_place = self.matrix, []
        indexgoal = range(len(goal))
        for i in indexgoal:
            if goal[i] != matrix[i] and matrix[i] != 0:
                not_in_place.append(matrix[i])

        return len(not_in_place)      

    def h(self):
        matrix, goal = self.matrix, self.goal.matrix
        indexrange = range(len(matrix))
        manhattan = 0
        for num in matrix:
            pos_matrix = matrix.index(num)
            y_matrix, x_matrix = divmod(pos_matrix, 3)
            pos_goal = goal.index(num)
            y_goal, x_goal = divmod(pos_goal, 3)
            manhattan += abs(x_matrix - x_goal) + abs(y_matrix - y_goal)

        return manhattan

    def f(self):
        return self.g + self.h()

    def expand(self):
        initial_string = self.to_string()
        depth = self.depth + 1
        node_up = AstarNode(initial_string, goal=self.goal, parent=self, depth=depth)
        node_down = AstarNode(initial_string, goal=self.goal, parent=self, depth=depth)
        node_left = AstarNode(initial_string, goal=self.goal, parent=self, depth=depth)
        node_right = AstarNode(initial_string, goal=self.goal, parent=self, depth=depth)
        return node_up.up(), node_down.down(), node_left.left(), node_right.right()
