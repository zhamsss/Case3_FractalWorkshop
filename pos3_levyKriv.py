import turtle as t

def levy(order: int, size: float) -> None:
    if order == 1:
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

levy(3, 50)
t.done()