from puzzle8 import Node

class StateList(list):
    """ simule set"""

    def append(self, node):
        if node not in self:
            super(StateList, self).append(node)

class OpenList(StateList):
    pass

class ClosedList(StateList):
    pass

class SuccList(list):

    def __init__(self, opened, closed):
        self.opened = opened
        self.closed = closed
        super(SuccList, self).__init__()
    
    def append(self, node):
        if node != False and node not in self.opened and node not in self.closed:
            super(StateList, self).append(node)
