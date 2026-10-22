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

dragon(3, 50)
t.done()