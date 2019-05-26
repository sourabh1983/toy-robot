import sys

from robot.position import InvalidCoordinates
from robot.robot import InvalidCommand, ToyRobot

bot = ToyRobot()


def robot_runner():
    print('Robot is ready to accept commands.')
    while True:
        try:
            command = input().strip()
            bot.action_on_robot(command)
        except (IndexError, InvalidCoordinates, InvalidCommand):
            print('Invalid command')
            continue


def read_commands_from_file():
    with open('testdata.txt') as command_file:
        for command in command_file:
            try:
                bot.action_on_robot(command.strip())
            except (IndexError, InvalidCoordinates, InvalidCommand):
                print('Invalid command')
                continue


if len(sys.argv) > 1:
    if sys.argv[1] == 'file':
        read_commands_from_file()
else:
    robot_runner()
