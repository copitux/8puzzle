from puzzle8 import Node

class StateList(list):
    """ simule set"""

    def append(self, node):
        if node not in self:
            super(StateList, self).append(node)
        else:
            print 'node is in list'

class OpenList(StateList):
    pass

class ClosedList(StateList):
    pass
