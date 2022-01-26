import time


class TrafficLight:
    _color = None

    def running(self):
        _color = 'Red'
        print(_color)
        time.sleep(7)
        _color = 'Yellow'
        print(_color)
        time.sleep(2)
        _color = 'Green'
        print(_color)
        time.sleep(10)


light = TrafficLight()

start = time.perf_counter()
while (start + 25) > time.perf_counter():
    light.running()
