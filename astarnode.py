from node import Node

class AstarNode(Node):

    def __init__(self, matrix=None, goal=None, parent=None, depth=0):
        super(AstarNode, self).__init__(matrix, depth)
        self.goal = goal
        self.parent = parent
        self.g = self.calcg()
        self.h = self.h()
    
    def calcg(self):
        #if self.parent is None:
        #    return self.heuristic_desorder()
        #else:
        #    return self.parent.g + self.heuristic_desorder()
        if self.parent is None:
            return 0
        else:
            return self.parent.g + 1

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
            if num != 0:
                pos_matrix = matrix.index(num)
                y_matrix, x_matrix = divmod(pos_matrix, 3)
                pos_goal = goal.index(num)
                y_goal, x_goal = divmod(pos_goal, 3)
                manhattan += abs(x_matrix - x_goal) + abs(y_matrix - y_goal)

        return manhattan

    def f(self):
        return self.g + self.h

    def expand(self):
        nodes = super(AstarNode, self).expand()
        depth = self.depth + 1
        node_left = AstarNode(nodes[0].to_string(), goal=self.goal, parent=self, depth=depth)
        node_up = AstarNode(nodes[1].to_string(), goal=self.goal, parent=self, depth=depth)
        node_right = AstarNode(nodes[2].to_string(), goal=self.goal, parent=self, depth=depth)
        node_down = AstarNode(nodes[3].to_string(), goal=self.goal, parent=self, depth=depth)

        return node_left, node_up, node_right, node_down
