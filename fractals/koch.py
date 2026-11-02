import turtle as t

def _koch_recursive(order, size):
    """Внутренняя рекурсивная функция для отрисовки кривой Коха."""
    if order == 0:
        t.forward(size)
        return
    _koch_recursive(order - 1, size / 3)
    t.left(60)
    _koch_recursive(order - 1, size / 3)
    t.right(120)
    _koch_recursive(order - 1, size / 3)
    t.left(60)
    _koch_recursive(order - 1, size / 3)
    
def koch(order, size):
    """Рисует Кривую Коха в удобном месте экрана."""
    t.up()
    t.goto(-size / 2, 0) 
    t.down()
    t.setheading(0)    
    _koch_recursive(order, size)    

def snowflake(order, size):
    """Рисует Снежинку Коха."""
    t.up()
    t.goto(-size / 2, size * (3 ** 0.5) / 6)
    t.down()
    t.setheading(0)   

    for _ in range(3):
        _koch_recursive(order, size)
        t.right(120)  


def _minkowski_recursive(order, size):
    """Внутренняя рекурсивная функция для отрисовки кривой Минковского."""
    if order == 0:
        t.forward(size)
        return

    _minkowski_recursive(order - 1, size / 4)
    t.left(90)
    _minkowski_recursive(order - 1, size / 4)
    t.right(90)
    _minkowski_recursive(order - 1, size / 4)
    t.right(90)
    _minkowski_recursive(order - 1, size / 4)
    _minkowski_recursive(order - 1, size / 4)
    t.left(90)
    _minkowski_recursive(order - 1, size / 4)
    t.left(90)
    _minkowski_recursive(order - 1, size / 4)
    t.right(90)
    _minkowski_recursive(order - 1, size / 4)
    
def minkowski(order, size):
    """Рисует Кривую Минковского в удобном месте экрана."""
    t.up()
    t.goto(-size / 2, 0) 
    t.down()
    t.setheading(0) 
    _minkowski_recursive(order, size)
