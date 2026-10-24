import turtle as t

def koch(order, size):
    if order == 0:
        t.forward(size)
        return
    koch(order - 1, size / 3)
    t.left(60)
    koch(order - 1, size / 3)
    t.right(120)
    koch(order - 1, size / 3)
    t.left(60)
    koch(order - 1, size / 3)
