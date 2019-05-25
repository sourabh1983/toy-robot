from .position import Position
from .table import TABLE


# My Toy robot needs a table and initial position
class ToyRobot:

    position = None

    # place robot on table
    def place(self, coordinates):
        self.position = Position(*coordinates)
    '''
    The robot is free to roam around the surface of the table, but
    must be prevented from falling to destruction
    Destructive move is when move command leads to negative
    coordinates or exceeding table dimensions
    '''
    def move(self):
        pass

    def left(self):
        pass

    def right(self):
        pass

    def report(self):
        pass
