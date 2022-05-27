from math import *


class Ship:
    """
    Ship is a class that create a instance which is a ship. Each ship has it's attributes.
    A ship  has 7 attributes:

    1. RADIUS : the radius of the ship, is a constant of the class.
    2. x_place : the position on the x-axis of the ship.
    3.x_speed : the speed on the x-axis of the ship.
    4.y_place : the speed on the y-axis of the ship.
    5. y_speed : the position on the y-axis of the ship.
    6. nose_direction : nose direction of the ship (on degrees).
    7. life : the amount of life the ship has {the default is: 3}
    """

    RADIUS = 1
    START_LIFE = 3
    RIGHT = "Right"
    LEFT = "Left"
    ANGLE_CHANGE = 7
    COMPLETE_CIRCLE = 360
    LOSE_LIFE_PER_LOOP = 1

    def __init__(self, x_place, x_speed, y_place, y_speed, nose_direction, life=START_LIFE):
        """
        A constructor for a Ship object
        :param  x_place : the position on the x-axis of the ship.
        :param x_speed : the speed on the x-axis of the ship.
        :param y_place : the speed on the y-axis of the ship.
        :param y_speed : the position on the y-axis of the ship.
        :param nose_direction : nose direction of the ship (on degrees).
        :param the amount of life the ship has {the default is: 3}
        """
        self.__x_place = x_place
        self.__x_speed = x_speed
        self.__y_place = y_place
        self.__y_speed = y_speed
        self.__nose_direction = nose_direction % self.COMPLETE_CIRCLE  # Saves the angle range from 0 to 360.
        self.__life = life

    def set_nose_direction(self, side):
        """
        A method that set nose direction to one side (RIGHT or LEFT)
        :param side: the side to set the nose direction towards, can be RIGHT or LEFT
        """
        if side == self.RIGHT:
            self.__nose_direction -= self.ANGLE_CHANGE
        if side == self.LEFT:
            self.__nose_direction += self.ANGLE_CHANGE
        self.__nose_direction = self.__nose_direction % self.COMPLETE_CIRCLE   # Saves the angle range from 0 to 360.

    def get_nose_direction(self):
        """
        A  method to get the nose direction of the ship.
        :return: the nose direction (on degrees).
        """
        return self.__nose_direction

    def get_life(self):
        """
        A  method to get the amount of life of the ship.
        :return: the amount of life of the ship (type: int).
        """
        return self.__life

    def set_life(self):
        """
        A method that set the amount of life of the ship if it loosed one life.
        """
        if self.__life != 0:
            self.__life -= self.LOSE_LIFE_PER_LOOP

    def set_speed(self):
        """
        A method that set the speed of the ship.
        """
        self.__x_speed += cos(radians(self.__nose_direction))
        self.__y_speed += sin(radians(self.__nose_direction))

    def set_place_x(self, new_spot_x):
        """
        A method that set the place of the ship on the x-axis.
        :param new_spot_x: the new place on the x-axis
        """
        self.__x_place = new_spot_x

    def set_place_y(self, new_spot_y):
        """
        A method that set the place of the ship on the y-axis.
        :param new_spot_y: the new place on the y-axis
        """
        self.__y_place = new_spot_y

    def get_speed_x(self):
        """
         A method to get the speed of the ship on the x-axis.
        :return: the speed of the ship on the x-axis.
        """
        return self.__x_speed

    def get_speed_y(self):
        """
         A method to get the speed of the ship on the y-axis.
        :return: the speed of the ship on the y-axis.
        """
        return self.__y_speed

    def get_place_x(self):
        """
        A method that return the place of the ship on the x-axis.
        :return:  the place of the ship on the x-axis.
        """
        return self.__x_place

    def get_place_y(self):
        """
        A method that return the place of the ship on the y-axis.
        :return:  the place of the ship on the y-axis.
        """
        return self.__y_place
