from robot.table import TABLE

length = [i for i in range(TABLE.LENGTH + 1)]
width = [i for i in range(TABLE.WIDTH + 1)]
direction = ['NORTH', 'SOUTH', 'EAST', 'WEST']


class Position:
    def __init__(self, x, y, facing):
        if int(x) in length and int(y) in width and facing in direction:
            self.x = int(x)
            self.y = int(y)
            self.facing = facing
            print('Robot placed successfully')
        else:
            raise InvalidCoordinates


class InvalidCoordinates(BaseException):
    pass
