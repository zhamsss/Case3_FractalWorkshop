import math
import turtle

from pos1_basic import draw_binary_tree, draw_branch


def ask_number(label: str, default: float, lower: float,
               upper: float | None = None, integer: bool = False):
    """Читает параметр в консоли. Максимальная глубина не ограничена."""
    limits = (f"от {lower:g}" if upper is None else f"{lower:g}–{upper:g}")
    while True:
        raw = input(f"{label} ({limits}) [{default:g}]: ").strip()
        if not raw:
            return default
        try:
            value = int(raw) if integer else float(raw.replace(",", "."))
            # int проверяется без перевода во float (в том числе очень большие числа).
            valid = (lower <= value and (upper is None or value <= upper))
            if valid and (integer or math.isfinite(value)):
                return value
        except ValueError:
            pass
        number_type = "целое число" if integer else "число"
        print(f"Ошибка: введите {number_type} {limits}.")


def fit_tree(depth: int, size: float, angle: float) -> float:
    """Если дерево не помещается в окне, пропорционально уменьшает его."""
    xs = [0.0]
    ys = [0.0]

    def trace(x: float, y: float, heading: float, order: int, length: float):
        a = math.radians(heading)
        x += math.cos(a) * length
        y += math.sin(a) * length
        xs.append(x)
        ys.append(y)
        if order:
            new_length = length * order / (order + 1)
            trace(x, y, heading - angle, order - 1, new_length)
            trace(x, y, heading + angle, order - 1, new_length)

    trace(0, 0, 90, depth, size)
    scale = 1.0
    for value, available in ((max(xs), 640), (-min(xs), 550),
                             (max(ys), 547), (-min(ys), 143)):
        if value > 0:
            scale = min(scale, available / value)
    return size * scale


def draw_selected(screen, choice: str, depth: int, size: float,
                  angle: float = 30) -> None:
    """Очищает прежний рисунок и показывает один выбранный фрактал."""
    if choice == "1":
        actual_size = fit_tree(depth, size, angle)
    else:
        actual_size = min(size, 670 / (depth + 2))

    if actual_size < size - 0.01:
        print(f"Размер уменьшен до {actual_size:.1f}, чтобы рисунок поместился в окне.")

    turtle.reset()
    screen.bgcolor("white")
    turtle.pencolor("black")
    turtle.pensize(1)
    turtle.shape("classic")
    turtle.showturtle()
    screen.tracer(1, 3)
    turtle.speed(6 if choice == "1" else 0)
    turtle.penup()
    if choice == "1":
        turtle.goto(-45, -202)
    else:
        turtle.goto(11, -331)
    turtle.setheading(90)
    turtle.pendown()

    print("Рисование началось. Результат появится в окне turtle...")
    if choice == "1":
        draw_binary_tree(depth, actual_size, angle)
    else:
        draw_branch(depth, actual_size)
        turtle.setheading(270)  # Направление указателя
    screen.update()
    print("Рисунок готов! Вернитесь в консоль Run в PyCharm: здесь уже доступно меню.")


def main() -> None:
    screen = None  # Не открываем пустое окно, пока пользователь не выбрал фрактал.
    try:
        while True:
            print()
            print("1. Двоичное дерево")
            print("2. Фрактал «Ветка»")
            print("3. Выход")
            choice = input("Ваш выбор: ").strip()

            if choice == "3":
                print("Выход из программы.")
                break
            if choice not in ("1", "2"):
                print("Ошибка: выберите 1, 2 или 3.")
                continue

            depth = ask_number("Глубина рекурсии", 4, 0, integer=True)
            size = ask_number("Размер", 185 if choice == "1" else 111, 10, 400)
            angle = ask_number("Угол (в градусах)", 30, 1, 85) if choice == "1" else 30

            if screen is None:
                screen = turtle.Screen()
                screen.setup(1280, 720)
                screen.title("Дерево и Ветка")
            draw_selected(screen, choice, depth, size, angle)

    except (EOFError, KeyboardInterrupt):
        print("\nВыход из программы.")
    except turtle.Terminator:
        print("\nОкно turtle закрыто. Программа завершена.")
    finally:
        if screen is not None:
            try:
                screen.bye()
            except (turtle.Terminator, turtle.TurtleGraphicsError):
                pass


if __name__ == "__main__":
    main()
