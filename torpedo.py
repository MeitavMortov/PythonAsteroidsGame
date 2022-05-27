class Torpedo:
    """
   Torpedo is a class that create a instance which is a torpedo. Each torpedo has it's attributes.
    A torpedo  has 7 attributes:

    1. RADIUS : the radius of the torpedo, is a constant of the class.
    2. x_place : the position on the x-axis of the torpedo.
    3.x_speed : the speed on the x-axis of the torpedo.
    4.y_place : the speed on the y-axis of the torpedo.
    5. y_speed : the position on the y-axis of the torpedo.
    6. direction : the direction of the torpedo (on degrees).
    7. counter : the counter of the life time of the torpedo.
    """
    RADIUS = 4
    COUNTER_PER_LOOP = 1

    def __init__(self, x_place, x_speed, y_place, y_speed, direction, counter=0):
        """
        A constructor for a Torpedo object
        :param  x_place : the position on the x-axis of the torpedo.
        :param x_speed : the speed on the x-axis of the torpedo.
        :param y_place : the position on the y-axis of the torpedo.
        :param y_speed : the speed on the y-axis of the torpedo.
        :param direction : the direction of the torpedo (on degrees).
        :param counter : the counter of the life time of the torpedo.{the default is: 0}
        """
        self.__x_place = x_place
        self.__x_speed = x_speed
        self.__y_place = y_place
        self.__y_speed = y_speed
        self.__direction = direction
        self.__counter = counter

    def get_counter(self):
        """
        A method to get the counter of life of the torpedo.
        :return: the counter of life of the torpedo.
        """
        return self.__counter

    def set_counter(self):
        """
        A method that set the counter of life of the torpedo.
        """
        self.__counter += self.COUNTER_PER_LOOP

    def set_place_x(self, new_spot_x):
        """
        A method that set the place of the torpedo on the x-axis.
        :param new_spot_x: the new place on the x-axis
        """
        self.__x_place = new_spot_x

    def set_place_y(self, new_spot_y):
        """
        A method that set the place of the torpedo on the y-axis.
        :param new_spot_y: the new place on the y-axis
        """
        self.__y_place = new_spot_y

    def get_speed_x(self):
        """
         A method to get the speed of the torpedo on the x-axis.
        :return: the speed of the torpedo on the x-axis.
        """
        return self.__x_speed

    def get_speed_y(self):
        """
         A method to get the speed of the torpedo on the y-axis.
        :return: the speed of the torpedo on the y-axis.
        """
        return self.__y_speed

    def get_place_x(self):
        """
        A method that return the place of the torpedo on the x-axis.
        :return:  the place of the torpedo on the x-axis.
        """
        return self.__x_place

    def get_place_y(self):
        """
        A method that return the place of the torpedo on the y-axis.
        :return:  the place of the torpedo on the y-axis.
        """
        return self.__y_place

    def get_direction(self):
        """
        A  method to get the nose direction of the torpedo.
        :return: the direction of the torpedo (on degrees).
        """
        return self.__direction
