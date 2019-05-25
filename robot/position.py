from robot.table import TABLE

length = [i for i in range(TABLE.LENGTH + 1)]
width = [i for i in range(TABLE.WIDTH + 1)]
direction = ['NORTH', 'SOUTH', 'EAST', 'WEST']


class Position:
    def __init__(self, x, y, facing):
        pass

class InvalidCoordinates(BaseException):
    pass
