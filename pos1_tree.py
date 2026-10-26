"""Роль 1: двоичное дерево.

Функция draw_binary_tree(depth, size, angle) предназначена для вызова
из общего меню проекта. Сама по себе при импорте ничего не рисует.
Перед вызовом установите начальную позицию и направление turtle.
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
                     match_gif: bool = False) -> None:
    """Двоичное дерево по заданию: size / 2. Для варианта GIF: match_gif=True."""
    if not isinstance(depth, int) or depth < 0:
        raise ValueError("Глубина должна быть целым числом от 0")
    if not 0 < size:
        raise ValueError("Длина должна быть больше нуля")
    if not 0 < angle < 90:
        raise ValueError("Угол должен быть от 1 до 89 градусов")
    _tree(depth, size, angle, match_gif)
