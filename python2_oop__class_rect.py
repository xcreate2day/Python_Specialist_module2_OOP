from typing import Self
from pprint import pprint


class Rect:
    def __init__(self, width: int | float = 0, height: int | float = 0):
        """ Init a new object of type Rect
            with params width, height both of type int or float
            Default values: width=0, height=0 """
        self.width = width
        self.height = height

    def area(self) -> int | float:
        """ Calculate area for current object Rect """
        return self.width * self.height

    def perimetr(self) -> int | float:
        """ Calculate perimetr for current object Rect """
        return (self.width + self.height) * 2

    def scale(self, times: int | float = 1) -> None:
        """ Change width and height, both scaled times """
        self.width *= times
        self.height *= times

    def rotate(self) -> None:
        """ Set width = height and height = width """
        self.width, self.height = self.height, self.width

    def __str__(self):
        return f'Rect: width is {self.width}, height is {self.height}'

    def __repr__(self):
        return f'Rect: width = {self.width}, height = {self.height}'

    def __eq__(self, other: Self):
        """ Compare 2 Rects by area and return bool """
        if type(other) == Rect:
            return (self.width == other.width) & (self.height == other.height)
        else:
            raise TypeError(f"{other} is not Rect")

    def __lt__(self, other: Self):
        """ Compare 2 Rects by area and return bool """
        if type(other) == Rect:
            return self.area() < other.area()
        else:
            raise TypeError(f"{other} is not Rect")

    def __gt__(self, other: Self):
        """ Compare 2 Rects by area and return bool"""
        if type(other) == Rect:
            return self.area() > other.area()
        else:
            raise TypeError(f"{other} is not Rect")


if __name__ == '__main__':
    """ width and height are supposed always to be positive numbers """
    new_rect = Rect(3, 4)
    another_rect_1 = Rect(3, 4)
    another_rect_2 = Rect(4, 3)
    another_rect_3 = Rect(2, 3)
    another_rect_4 = Rect(7, 3)
    rects = [new_rect, another_rect_1, another_rect_2, another_rect_3, another_rect_4]

    print("Check __str__: ", str(new_rect) == f'Rect: width is {new_rect.width}, height is {new_rect.height}')
    print(f'{new_rect!s}\n')

    print("Check __repr__: ", repr(new_rect) == f'Rect: width = {new_rect.width}, height = {new_rect.height}')
    print(f'{new_rect!r}\n')

    print("Check area: ", new_rect.area() == 3 * 4)
    print(new_rect.area(), '\n')

    print("Check perimetr: ", new_rect.perimetr() == (3 + 4) * 2)
    print(new_rect.perimetr(), '\n')

    print(new_rect)
    new_rect.scale(10)
    print("Check scale 10: ", (new_rect.width == 3 * 10) & (new_rect.height == 4 * 10))
    print(new_rect)
    new_rect.scale(0.1)
    print("Check scale 0.1: ", (new_rect.width == 30 * 0.1) & (new_rect.height == 40 * 0.1))
    print(f'{new_rect!s}\n')

    new_rect.rotate()
    print("Check rotate: ", (new_rect.width == 4) & (new_rect.height == 3))
    print(f'{new_rect!s}\n')

    print("Check __eq__: False, True")
    print(new_rect == another_rect_1)
    print(new_rect == another_rect_2)
    # print(new_rect == 10)
    assert new_rect == another_rect_2, "Rects have different areas"
    assert not new_rect == another_rect_4, "Rects have different areas"
    print()

    print("Check __lt__: False, False, True")
    print(new_rect < another_rect_1)
    print(new_rect < another_rect_3)
    print(new_rect < another_rect_4)
    print()

    print("Check __gt__: False, True, False")
    print(new_rect > another_rect_1)
    print(new_rect > another_rect_3)
    print(new_rect > another_rect_4)
    print()

    # sorted_rects = sorted(rects)
    # print('Sorted rects: ', *sorted_rects, sep=', ')
    print(f'Sorted rects: {sorted(rects)}')  # __repr__()
    print(f'Max rect: {max(rects)!r}')
    print(f'Min rect: {min(rects)!r}')
    print()

    pprint('__ne__' in dir(new_rect))
    print("dict:")
    pprint(Rect.__dict__)
