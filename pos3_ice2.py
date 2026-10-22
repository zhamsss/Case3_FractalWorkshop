import turtle as t

def ice_fractal_2(order: int, size: float) -> None:
    if order == 1:
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

ice_fractal_2(3, 50)
t.done()