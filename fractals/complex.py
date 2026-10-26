import turtle as t

def dragon(order: int, size: float) -> None:
    if order == 1:
        t.left(45)
        t.forward(size)
        t.right(90)
        t.forward(size)
        return
    if order == 2:
        t.left(45)
        dragon(order - 1, size)
        t.right(90)
        t.forward(size)
        t.left(90)
        t.forward(size)
        return
    t.left(45)
    dragon(order - 1, size)
    t.right(135)
    dragon(order - 2, size)
    t.left(45)
    dragon(order - 2, size)
import turtle as t

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
import turtle as t

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
import turtle as t

def levy(order: int, size: float) -> None:
    if order == 0:
        t.left(45)
        t.forward(size)
        t.right(90)
        t.forward(size)
        t.left(45)
        return

    t.left(45)
    levy(order - 1, size)
    t.right(90)
    levy(order - 1, size)
    t.left(45)
