import turtle as t
import math

def dragon(order: int, size: float, sign: int = 1) -> None:
    if order == 0:
        t.forward(size)
        return

    next_size = size / math.sqrt(2)
    
    t.left(45 * sign)
    dragon(order - 1, next_size, 1)
    t.right(90 * sign)
    dragon(order - 1, next_size, -1)
    t.left(45 * sign)


def ice_fractal_1(order: int, size: float) -> None:
    if order == 0:
        t.forward(size)
        t.left(90)
        t.forward(size / 2)
        t.left(180)
        t.forward(size / 2)
        t.left(90)
        t.forward(size)
        return
    ice_fractal_1(order - 1, size)
    t.left(90)
    ice_fractal_1(order - 1, size / 2)
    t.left(180)
    ice_fractal_1(order - 1, size / 2)
    t.left(90)
    ice_fractal_1(order - 1, size)


def ice_fractal_2(order: int, size: float) -> None:
    if order == 0:
        t.forward(size)
        t.left(115)
        t.forward(size / 2)
        t.left(180)
        t.forward(size / 2)
        t.left(65 + 65)
        t.forward(size / 2)
        t.left(180)
        t.forward(size / 2)
        t.left(115)
        t.forward(size)
        return

    ice_fractal_2(order - 1, size)
    t.left(115)
    ice_fractal_2(order - 1, size / 2)
    t.left(180)
    ice_fractal_2(order - 1, size / 2)
    t.left(130)
    ice_fractal_2(order - 1, size / 2)
    t.left(180)
    ice_fractal_2(order - 1, size / 2)
    t.left(115)
    ice_fractal_2(order - 1, size)


def levy(order: int, size: float) -> None:
    if order == 0:
        t.forward(size)
        return

    next_size = size / math.sqrt(2)
    
    t.left(45)
    levy(order - 1, next_size)
    t.right(90)
    levy(order - 1, next_size)
    t.left(45)
