import turtle as t

def ice_fractal_1(order: int, size: float) -> None:
    if order == 1:
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
