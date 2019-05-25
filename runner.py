from robot.position import InvalidCoordinates
from robot.robot import ToyRobot


def robot_runner():
    print('Your robot is ready to accept commands.')
    while True:
        try:
            action = input()
            bot.action_on_robot(action)
        except (IndexError, InvalidCoordinates):
            print('Invalid command')
            continue


bot = ToyRobot()

robot_runner()
