def draw_header(title):
    print("=" * 40)
    print(title.center(40))
    print("=" * 40)


def draw_menu(options_list):
    print("\nОберіть дію:")
    
    for i, option in enumerate(options_list, 1):
        print(f"[ {i} ] {option}")


def draw_warning(message):
    print("\n" + "!" * 40)
    print(message.center(40))
    print("!" * 40)