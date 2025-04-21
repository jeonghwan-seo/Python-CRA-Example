class Rectangle:
    def __init__(self):
        self._width = 0
        self._height = 0

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def area(self):
        return self._width * self._height


class Square(Rectangle):
    def set_width(self, width):
        super().set_width(width)
        super().set_height(width)  # 정사각형이므로 높이도 설정

    def set_height(self, height):
        super().set_width(height)  # 정사각형이므로 너비도 설정
        super().set_height(height)
