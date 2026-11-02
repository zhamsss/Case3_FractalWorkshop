def finish_drawing() -> None:
    """Обновление экрана и ожидание возврата в меню."""
    turtle.penup()
    turtle.update()
    print("\nРисование завершено!")
    input("Нажмите Enter в консоли, чтобы вернуться в меню...")


def main():
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
            size = ask_float("Размер ствола (10-500): ", *LIMITS["size"])
            angle = ask_float("Угол ветвления (1-89): ", *LIMITS["angle"])
            print("Рисую...", flush=True)
            reset_canvas("forestgreen")
            start_place(0, -250, 90)
            draw_tree(depth, size, angle)
            finish_drawing()

        elif choice == "2":
            depth = ask_int("Глубина рекурсии (1-10): ", *LIMITS["branch_depth"])
            size = ask_float("Размер ветки (10-500): ", *LIMITS["size"])
            print("Рисую...", flush=True)
            reset_canvas("darkgreen")
            start_place(0, -250, 90)
            draw_branch(depth, size)
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
