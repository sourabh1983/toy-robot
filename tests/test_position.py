import pytest

from robot.position import InvalidCoordinates, Position


@pytest.mark.parametrize(
    'x, y, facing',
    [
        (1, 1, 'NORTH'),
        (0, 1, 'EAST'),
        (0, 2, 'SOUTH'),
    ]
)
def test_valid_position(x, y, facing):
    position = Position(x, y, facing)
    assert position.x == x
    assert position.y == y
    assert position.facing == facing


@pytest.mark.parametrize(
    'x, y, facing',
    [
        (-1, 1, 'NORTH'),
        (0, 6, 'EAST'),
        (0, 2, 'XXX'),
    ]
)
def test_invalid_position(x, y, facing):
    with pytest.raises(InvalidCoordinates):
        Position(x, y, facing)
