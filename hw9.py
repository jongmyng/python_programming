# -*- coding: utf-8 -*-
"""hw9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FdDtBowqLky08YaFpqtMbQx6QYjG66Z3
"""

class Rectangle:
    def __init__(a, x1, y1, x2, y2):
        a.x1 = x1
        a.y1 = y1
        a.x2 = x2
        a.y2 = y2

    def getArea(a):
        w = abs(a.x2 - a.x1)
        h = abs(a.y2 - a.y1)
        return w * h

    def getPerimeter(a):
        w = abs(a.x2 - a.x1)
        h = abs(a.y2 - a.y1)
        return 2 * (w + h)

    def show(a):
        print(f'좌측 상단 꼭지점이 ({a.x1}, {a.y1})이고 우측 하단 꼭지점이 ({a.x2}, {a.y2})인 사각형입니다.')

r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')

