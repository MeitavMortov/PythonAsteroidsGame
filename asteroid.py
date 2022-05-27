class Asteroid:
    """
    Asteroid is a class that create a instance which is a asteroid. Each asteroid has it's attributes.
    A asteroid  has 5 attributes:
    1. x_place : the position on the x-axis of the asteroid.
    2. x_speed : the speed on the x-axis of the asteroid.
    3. y_place : the speed on the y-axis of the asteroid.
    4. y_speed : the position on the y-axis of the asteroid.
    5. size : the size of the asteroid.
    """

    def __init__(self, x_place, x_speed, y_place, y_speed, size):
        """
        A constructor for a Asteroid object
        :param  x_place : the position on the x-axis of the asteroid.
        :param x_speed : the speed on the x-axis of the asteroid.
        :param y_place : the speed on the y-axis of the asteroid.
        :param y_speed : the position on the y-axis of the asteroid.
        :param size : the size of the asteroid.
        """
        self.__x_place = x_place
        self.__x_speed = x_speed
        self.__y_place = y_place
        self.__y_speed = y_speed
        self.__size = size
        self.__radius = self.__size * 10 - 5

    def has_intersection(self, obj):
        """
        this method checks if the asteroid has intersection with a object.
        :param obj: an object
        :return: True if the asteroid has intersection with the object, else: False.
        """
        distance = ((obj.get_place_x() - self.__x_place) ** 2 + (obj.get_place_y() - self.__y_place) ** 2) ** 0.5
        if distance <= self.__radius + obj.RADIUS:
            return True
        return False

    def get_radius(self):
        """
        A method to get the radius of the asteroid.
        :return: the radius of the asteroid.
        """
        return self.__radius

    def get_size(self):
        """
        A method to get the size of the asteroid.
        :return: the size of the asteroid.
        """
        return self.__size

    def set_place_x(self, new_spot_x):
        """
        A method that set the place of the asteroid on the x-axis.
        :param new_spot_x: the new place on the x-axis
        """
        self.__x_place = new_spot_x

    def set_place_y(self, new_spot_y):
        """
        A method that set the place of the asteroid on the y-axis.
        :param new_spot_y: the new place on the y-axis
        """
        self.__y_place = new_spot_y

    def get_speed_x(self):
        """
         A method to get the speed of the asteroid on the x-axis.
        :return: the speed of the asteroid on the x-axis.
        """
        return self.__x_speed

    def get_speed_y(self):
        """
         A method to get the speed of the asteroid on the y-axis.
        :return: the speed of the asteroid on the y-axis.
        """
        return self.__y_speed

    def get_place_x(self):
        """
        A method that return the place of the asteroid on the x-axis.
        :return:  the place of the asteroid on the x-axis.
        """
        return self.__x_place

    def get_place_y(self):
        """
        A method that return the place of the asteroid on the y-axis.
        :return:  the place of the asteroid on the y-axis.
        """
        return self.__y_place
