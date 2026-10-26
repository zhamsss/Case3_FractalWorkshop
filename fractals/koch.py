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

def snowflake(order, size):
    t.up()
    t.goto(-size / 2, size * (3 ** 0.5) / 6)
    t.down()
    t.setheading(0)   

    for _ in range(3):
        koch(order, size)
        t.right(120)  
import turtle as t

def minkowski(order, size):
    if order == 0:
        t.forward(size)
        return

    minkowski(order - 1, size / 4)
    t.left(90)
    minkowski(order - 1, size / 4)
    t.right(90)
    minkowski(order - 1, size / 4)
    t.right(90)
    minkowski(order - 1, size / 4)
    minkowski(order - 1, size / 4)
    t.left(90)
    minkowski(order - 1, size / 4)
    t.left(90)
    minkowski(order - 1, size / 4)
    t.right(90)
    minkowski(order - 1, size / 4)
