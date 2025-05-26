class xy_info:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class xyManager:
    def __init__(self):
        self._arr = []

    def add(self, data: xy_info):
        self._arr.append(data)

    def drawing(self):
        for o in self._arr:
            print(f"{o.x}, {o.y} 에 버튼 찍힘")


a = xyManager()
a.add(xy_info(1, 2))
a.add(xy_info(2, 3))
a.add(xy_info(5, 5))
a.add(xy_info(7, 1))
a.drawing()
