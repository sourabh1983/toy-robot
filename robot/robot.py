from .position import Position
from .table import TABLE


def is_robot_placed(func):
    def placed(self):
        if self.position is None:
            print('Robot is not placed')
            return False
        func(self)
    return placed


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
    @is_robot_placed
    def move(self):
        if self.position.facing == 'NORTH' and self.position.y < TABLE.WIDTH:
            self.position.y = self.position.y + 1
        elif self.position.facing == 'SOUTH' and self.position.y != 0:
            self.position.y = self.position.y - 1
        elif self.position.facing == 'EAST' and self.position.x < TABLE.LENGTH:
            self.position.x = self.position.x + 1
        elif self.position.facing == 'WEST' and self.position.x != 0:
            self.position.x = self.position.x - 1

    @is_robot_placed
    def left(self):
        self.position.facing = {
            'NORTH': 'WEST',
            'WEST': 'SOUTH',
            'SOUTH': 'EAST',
            'EAST': 'NORTH'
        }.get(self.position.facing)

    @is_robot_placed
    def right(self):
        self.position.facing = {
            'NORTH': 'EAST',
            'EAST': 'SOUTH',
            'SOUTH': 'WEST',
            'WEST': 'NORTH'
        }.get(self.position.facing)

    def report(self):
        print(
            f'Output: {self.position.x}, \
                      {self.position.y}, \
                      {self.position.facing}'
        )
        return (self.position.x, self.position.y, self.position.facing)

    def action_on_robot(self, action):
        action = action.split()
        if action[0] == 'PLACE':
            position = tuple(action[1].split(','))
            self.place(position)
        elif action[0] == 'MOVE':
            self.move()
        elif action[0] == 'LEFT':
            self.left()
        elif action[0] == 'RIGHT':
            self.right()
        elif action[0] == 'REPORT':
            self.report()
