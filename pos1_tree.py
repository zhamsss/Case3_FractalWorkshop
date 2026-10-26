"""Рекурсивное построение двоичного дерева с помощью turtle."""

import turtle


def _draw_tree(depth: int, size: float, angle: float, gradual_reduction: bool) -> None:
    """Рекурсивно рисует дерево, затем возвращается к основанию."""
    if depth == 0:
        turtle.forward(size)
        turtle.backward(size)
        return

    turtle.forward(size)
    turtle.right(angle)
    # По умолчанию каждый следующий отрезок вдвое короче предыдущего.
    next_size = size * depth / (depth + 1) if gradual_reduction else size / 2
    _draw_tree(depth - 1, next_size, angle, gradual_reduction)
    turtle.left(2 * angle)
    _draw_tree(depth - 1, next_size, angle, gradual_reduction)
    turtle.right(angle)
    turtle.backward(size)


def draw_binary_tree(depth: int, size: float, angle: float, *,
                     gradual_reduction: bool = False) -> None:
    """Рисует дерево. При gradual_reduction=True ветви укорачиваются плавно."""
    if not isinstance(depth, int) or depth < 0:
        raise ValueError("Глубина должна быть целым числом от 0")
    if not 0 < size:
        raise ValueError("Длина должна быть больше нуля")
    if not 0 < angle < 90:
        raise ValueError("Угол должен быть от 1 до 89 градусов")
    _draw_tree(depth, size, angle, gradual_reduction)
