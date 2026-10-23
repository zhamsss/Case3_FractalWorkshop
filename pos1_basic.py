"""Роль 1. Рекурсивные фракталы из кейса

Публичные функции:
    draw_binary_tree(depth, size, angle) - дерево
    draw_branch(n, size) - фрактал «Ветка»


"""

import turtle


def _tree(depth: int, size: float, angle: float, match_gif: bool) -> None:
    """Рекурсивно рисует дерево, затем возвращается к основанию."""
    if depth == 0:
        turtle.forward(size)
        turtle.backward(size)
        return

    turtle.forward(size)
    turtle.right(angle)
    # GIF: длины 5, 4, 3, 2, 1 (при depth=4).
    # В тексте кейса: каждая следующая ветка вдвое короче.
    next_size = size * depth / (depth + 1) if match_gif else size / 2
    _tree(depth - 1, next_size, angle, match_gif)
    turtle.left(2 * angle)
    _tree(depth - 1, next_size, angle, match_gif)
    turtle.right(angle)
    turtle.backward(size)


def draw_binary_tree(depth: int, size: float, angle: float, *,
                     match_gif: bool = True) -> None:
    """Двоичное дерево. Для точного правила size/2: match_gif=False."""
    if not isinstance(depth, int) or depth < 0:
        raise ValueError("Глубина должна быть целым числом от 0")
    if not 0 < size:
        raise ValueError("Длина должна быть больше нуля")
    if not 0 < angle < 90:
        raise ValueError("Угол должен быть от 1 до 89 градусов")
    _tree(depth, size, angle, match_gif)


def _shoot(order: int, length: float) -> None:
    """Прямой побег с небольшими парными отростками"""
    if order <= 1:
        turtle.forward(length)
        turtle.backward(length)
        return

    # Чем больше порядок, тем больше пар "усиков" вдоль побега.
    # Их основания располагаются на 1/2 длины (order=2), на 0.3
    # и 0.6 длины (order=3), и т.д.
    fractions = [i / (order + (0.35 if order >= 3 else 0.0))
                 for i in range(1, order)]
    previous = 0.0
    for fraction in fractions:
        turtle.forward(length * (fraction - previous))
        tiny = length * 0.15
        turtle.left(45)
        turtle.forward(tiny)
        turtle.backward(tiny)
        turtle.right(90)
        turtle.forward(tiny)
        turtle.backward(tiny)
        turtle.left(45)
        previous = fraction
    turtle.forward(length * (1 - previous))
    turtle.backward(length)


def _diagonal_branch(level: int, step: float, base_size: float,
                     axis: float, side: int, max_shoot: float | None = None) -> None:
    """Диагональная ветка с вертикальными и горизонтальными побегами."""
    turtle.forward(step)
    if level >= 2:
        diagonal_heading = turtle.heading()
        shoot_size = 0.20 * base_size * (level - 1)
        if max_shoot is not None:
            shoot_size = min(shoot_size, max_shoot)
        # Рисуем вертикальный побег и горизонтальный побег наружу.
        turtle.setheading(axis)
        _shoot(level - 1, shoot_size)
        turtle.setheading(axis + side * 90)
        _shoot(level - 1, shoot_size)
        turtle.setheading(diagonal_heading)

    if level > 0:
        _diagonal_branch(level - 1, step, base_size, axis, side, max_shoot)
    turtle.backward(step)


def draw_branch(n: int, size: float) -> None:
    """«Ветка»: вертикальный ствол, симметричные диагонали и побеги.

    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Глубина должна быть целым числом от 0")
    if not 0 < size:
        raise ValueError("Длина должна быть больше нуля")

    # На глубине 5+ длинные побеги начинают пересекать соседние ярусы.
    # При n <= 4 геометрия остаётся точно такой же, как в образце.
    max_shoot = None if n <= 4 else (2.6 / n) * size

    def grow(level: int) -> None:
        if level == 0:
            turtle.forward(size * 2)
            turtle.backward(size * 2)
            return

        axis = turtle.heading()
        turtle.forward(size)
        # От основания к верхушке длина парных диагоналей убывает.
        step = 0.5 * size * level / (level + 1)
        turtle.setheading(axis + 45)
        _diagonal_branch(level, step, size, axis, +1, max_shoot)
        turtle.setheading(axis - 45)
        _diagonal_branch(level, step, size, axis, -1, max_shoot)
        turtle.setheading(axis)
        grow(level - 1)
        turtle.backward(size)

    grow(n)
