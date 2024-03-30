HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечататьвсе добавленные задачи."""

tasks = []

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(tasks)
    elif command == "add":
        tasks = input("Введите название задачи: ")
        tasks.append(tasks)
        print("Задача добавлена")
    else:
        print("Неизвестная команда")
        break

print("До свидания!")