"""Единый интерфейс «Фрактальная мастерская» для Роли 4.

Файл должен лежать в корне репозитория рядом с файлами pos*.py
"""

import turtle

# =====================================================================
# ИМПОРТ ФУНКЦИЙ ИЗ ФАЙЛОВ КОЛЛЕГ
# Если у коллег функции называются иначе, измените имя после "import"
# =====================================================================
try:
    from pos1_tree import draw_binary_tree as _draw_tree
except ImportError:
    # Альтернативное имя, если назвали просто draw_tree
    from pos1_tree import _draw_tree

from pos1_branch import draw_branch

try:
    from pos2_koch import koch
except ImportError:
    from pos2_koch import draw_koch as koch

try:
    from pos2_koch_snowflake import koch_snowflake
except ImportError:
    from pos2_koch_snowflake import draw_snowflake as koch_snowflake

try:
    from pos2_minkowski import minkowski
except ImportError:
    from pos2_minkowski import draw_minkowski as minkowski

try:
    from pos3_ice1 import ice_fractal_1
except ImportError:
    from pos3_ice1 import ice_1 as ice_fractal_1

try:
    from pos3_ice2 import ice_fractal_2
except ImportError:
    from pos3_ice2 import ice_2 as ice_fractal_2

try:
    from pos3_levyKriv import levy
except ImportError:
    from pos3_levyKriv import draw_levy as levy

try:
    from pos3_dragon_oogway import dragon
except ImportError:
    from pos3_dragon_oogway import draw_dragon as dragon


# Настройки ограничений, чтобы программа не зависала и не падала
LIMITS = {
    "tree_depth": (1, 12),
    "branch_depth": (1, 10),
    "koch_order": (0, 5),
    "snowflake_order": (0, 5),
    "minkowski_order": (0, 4),
    "ice_order": (0, 4),
    "levy_order": (0, 12),
    "dragon_order": (0, 13),
    "angle": (0.0, 180.0),
    "size": (10.0, 500.0),
    "segment": (1.0, 50.0),
}

# Включить быструю отрисовку без анимации перемещений? 
# True - мгновенно, False - черепашка ползает плавно.
USE_INSTANT_DRAW = True 


def ask_int(prompt: str, min_val: int, max_val: int) -> int:
    """Безопасный ввод целого числа."""
    while True:
        try:
            val = int(input(prompt).strip())
            if min_val <= val <= max_val:
                return val
            print(f"Ошибка: введите число в диапазоне от {min_val} до {max_val}.")
        except ValueError:
            print("Ошибка: требуется целое число.")


def ask_float(prompt: str, min_val: float, max_val: float) -> float:
    """Безопасный ввод вещественного числа."""
    while True:
        try:
            val = float(input(prompt).strip().replace(",", "."))
            if min_val <= val <= max_val:
                return val
            print(f"Ошибка: введите число в диапазоне от {min_val} до {max_val}.")
        except ValueError:
            print("Ошибка: требуется число (например, 150 или 45.5).")


def show_menu() -> None:
    print("\n" + "="*30)
    print("=== ФРАКТАЛЬНАЯ МАСТЕРСКАЯ ===")
    print("="*30)
    print("1. Двоичное дерево")
    print("2. Фрактал 'Ветка'")
    print("3. Кривая Коха")
    print("4. Снежинка Коха")
    print("5. Кривая Минковского")
    print("6. Ледяной фрактал №1")
    print("7. Ледяной фрактал №2")
    print("8. Кривая Леви")
    print("9. Дракон Хартера-Хейтуэя")
    print("10. Выход")
    print("="*30)


def reset_canvas(color: str = "black") -> None:
    """Сброс экрана и подготовка черепашки."""
    turtle.reset()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.pensize(1)
    turtle.pencolor(color)
    if USE_INSTANT_DRAW:
        turtle.tracer(0, 0)
    else:
        turtle.tracer(1, 10)


def start_place(x: float, y: float, heading: float) -> None:
    """Установка стартовой позиции без рисования линий."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(heading)
    turtle.pendown()


def finish_drawing() -> None:
    """Обновление экрана и ожидание возврата в меню."""
    turtle.penup()
    turtle.update()
    print("\nРисование завершено!")
    input("Нажмите Enter в консоли, чтобы вернуться в меню...")


def main():
    # Создаем окно один раз при старте
    screen = turtle.Screen()
    screen.title("Фрактальная мастерская — Итог")
    screen.setup(width=900, height=750)
    
    while True:
        show_menu()
        choice = input("Выберите пункт меню (1-10): ").strip()
        
        if choice == "10":
            print("Выход из программы. До свидания!")
            break
            
        elif choice == "1":
            depth = ask_int("Глубина рекурсии (1-12): ", *LIMITS["tree_depth"])
            size = ask_float("Размер ствола (10-400): ", *LIMITS["size"])
            angle = ask_float("Угол ветвления (0-180): ", *LIMITS["angle"])
            print("Рисую...", flush=True)
            reset_canvas("forestgreen")
            start_place(0, -250, 90) # Дерево растет снизу вверх (90 градусов)
            draw_tree(depth, size, angle)
            finish_drawing()

        elif choice == "2":
            depth = ask_int("Глубина рекурсии (1-10): ", *LIMITS["branch_depth"])
            size = ask_float("Размер ветки (10-400): ", *LIMITS["size"])
            angle = ask_float("Угол отклонения (0-180): ", *LIMITS["angle"])
            print("Рисую...", flush=True)
            reset_canvas("darkgreen")
            start_place(0, -250, 90)
            draw_branch(depth, size, angle)
            finish_drawing()

        elif choice == "3":
            order = ask_int("Порядок кривой (0-5): ", *LIMITS["koch_order"])
            size = ask_float("Общая длина (10-500): ", *LIMITS["size"])
            print("Рисую...", flush=True)
            reset_canvas("blue")
            start_place(-size / 2, 100, 0)
            koch(order, size)
            finish_drawing()

        elif choice == "4":
            order = ask_int("Порядок снежинки (0-5): ", *LIMITS["snowflake_order"])
            size = ask_float("Длина стороны (10-500): ", *LIMITS["size"])
            print("Рисую...", flush=True)
            reset_canvas("royalblue")
            # Смещение, чтобы центрировать треугольник
            start_place(-size / 2, size * 0.3, 0)
            koch_snowflake(order, size)
            finish_drawing()

        elif choice == "5":
            order = ask_int("Порядок кривой (0-4): ", *LIMITS["minkowski_order"])
            size = ask_float("Общая длина (10-500): ", *LIMITS["size"])
            print("Рисую...", flush=True)
            reset_canvas("purple")
            start_place(-size / 2, 0, 0)
            minkowski(order, size)
            finish_drawing()

        elif choice == "6":
            order = ask_int("Порядок фрактала (0-4): ", *LIMITS["ice_order"])
            size = ask_float("Общая длина (10-500): ", *LIMITS["size"])
            print("Рисую...", flush=True)
            reset_canvas("teal")
            start_place(-size / 2, 0, 0)
            ice_fractal_1(order, size)
            finish_drawing()

        elif choice == "7":
            order = ask_int("Порядок фрактала (0-4): ", *LIMITS["ice_order"])
            size = ask_float("Общая длина (10-500): ", *LIMITS["size"])
            print("Рисую...", flush=True)
            reset_canvas("darkcyan")
            start_place(-size / 2, 0, 0)
            ice_fractal_2(order, size)
            finish_drawing()

        elif choice == "8":
            order = ask_int("Порядок кривой (0-12): ", *LIMITS["levy_order"])
            size = ask_float("Длина одного шага (1-50): ", *LIMITS["segment"])
            print("Рисую...", flush=True)
            reset_canvas("crimson")
            start_place(-100, -50, 0)
            levy(order, size)
            finish_drawing()

        elif choice == "9":
            order = ask_int("Порядок дракона (0-13): ", *LIMITS["dragon_order"])
            size = ask_float("Длина одного шага (1-50): ", *LIMITS["segment"])
            print("Рисую...", flush=True)
            reset_canvas("darkred")
            start_place(-150, 50, 0)
            dragon(order, size)
            finish_drawing()

        else:
            print("Неверный пункт. Выберите число от 1 до 10.")
            
    turtle.bye()


if __name__ == "__main__":
    try:
        main()
    except turtle.Terminator:
        print("\nОкно анимации было закрыто.")
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем.")
