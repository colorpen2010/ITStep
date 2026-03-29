import task_16_subtask_2_1 as console_ui

console_ui.draw_header("СУПЕР ГРА 2024")

menu = [
    "Нова гра",
    "Завантажити збереження",
    "Вихід"
]

console_ui.draw_menu(menu)

choice = input("\nВаш вибір: ")

if choice not in ["1", "2", "3"]:
    console_ui.draw_warning("Неправильний вибір!")
else:
    print("Ви обрали пункт:", choice)