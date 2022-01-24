class Road:
    length = 1000
    width = 4

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_count_t(self):
        return self._length * self._width * 25 * 5 / 1000


my_road_1 = Road(2000, 10)
print(my_road_1)
print(my_road_1._width)
print(my_road_1._length)
print(my_road_1.asphalt_count_t())
