import pytest

from robot.robot import InvalidCommand, ToyRobot


def test_place():
    bot = ToyRobot()
    position = (0, 0, 'NORTH')
    bot.place(position)
    assert bot.position.x == 0
    assert bot.position.y == 0
    assert bot.position.facing == 'NORTH'
    assert (0, 0, 'NORTH') == bot.report()


def test_move():
    bot = ToyRobot()
    position = (0, 0, 'NORTH')
    bot.place(position)
    bot.move()
    assert bot.position.x == 0
    assert bot.position.y == 1
    assert bot.position.facing == 'NORTH'
    assert (0, 1, 'NORTH') == bot.report()


def test_left():

    bot = ToyRobot()
    position = (0, 0, 'NORTH')
    bot.place(position)
    bot.left()
    assert bot.position.x == 0
    assert bot.position.y == 0
    assert bot.position.facing == 'WEST'
    assert (0, 0, 'WEST') == bot.report()


def test_right():

    bot = ToyRobot()
    position = (0, 0, 'NORTH')
    bot.place(position)
    bot.right()
    assert bot.position.x == 0
    assert bot.position.y == 0
    assert bot.position.facing == 'EAST'
    assert (0, 0, 'EAST') == bot.report()


def test_action_on_robot():

    bot = ToyRobot()
    position = (0, 0, 'NORTH')
    bot.place(position)
    bot.action_on_robot('PLACE 0,0,NORTH')
    assert bot.position.x == 0
    assert bot.position.y == 0
    assert bot.position.facing == 'NORTH'
    assert (0, 0, 'NORTH') == bot.report()
    bot.action_on_robot('MOVE')
    assert bot.position.x == 0
    assert bot.position.y == 1
    assert bot.position.facing == 'NORTH'
    assert (0, 1, 'NORTH') == bot.report()
    bot.action_on_robot('LEFT')
    assert bot.position.x == 0
    assert bot.position.y == 1
    assert bot.position.facing == 'WEST'
    assert (0, 1, 'WEST') == bot.report()
    bot.action_on_robot('RIGHT')
    assert bot.position.x == 0
    assert bot.position.y == 1
    assert bot.position.facing == 'NORTH'
    assert (0, 1, 'NORTH') == bot.report()


@pytest.mark.parametrize(
    'place, action, position',
    [
        ((0, 0, 'NORTH'), ['MOVE', 'MOVE', 'LEFT'], (0, 2, 'WEST')),
        ((0, 1, 'NORTH'), ['MOVE'], (0, 2, 'NORTH')),
        ((0, 2, 'NORTH'), ['LEFT'], (0, 2, 'WEST')),
        ((0, 3, 'NORTH'), ['LEFT', 'MOVE', 'MOVE', 'RIGHT'], (0, 3, 'NORTH')),
        ((5, 5, 'NORTH'), ['MOVE', 'MOVE', 'MOVE', 'RIGHT'], (5, 5, 'EAST')),
    ]
)
def test_robot_movement(place, action, position):
    bot = ToyRobot()
    bot.place(place)
    for act in action:
        bot.action_on_robot(act)

    assert (
        bot.position.x, bot.position.y, bot.position.facing
    ) == position
    assert (
        bot.position.x, bot.position.y, bot.position.facing
    ) == bot.report()


@pytest.mark.parametrize(
    'command',
    [
        'PLACE 1, 1, NORTH',   # Invalid because spaces after comma
        'MOV',
        'XYZ',
        'PLACE 1,1',
        'PLACE 1,1,1,1,1'
    ]
)
def test_invalid_commands(command):
    bot = ToyRobot()
    with pytest.raises(InvalidCommand):
        bot.action_on_robot(command)
