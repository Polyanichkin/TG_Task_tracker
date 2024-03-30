HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - закончить запись задач"""

today = []
tomorrow = []
other_date = []

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print("Задачи на сегодня: ", today)
        print("Задачи на завтра: ", tomorrow)
        print("Задачи на другие даты: ", other_date)
    elif command == "add":
        task = input("Введите название задачи: ")
        date = input("Введите дату (Сегодня, Завтра, или другую дату в формате ЧЧ.ММ.ГГГГ: ")
        if date == "Сегодня":
                today.append(task)
        elif date == "Завтра":
                tomorrow.append(task)
        else:
            other_date.append(task)
        print("Задача добавлена")
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неизвестная команда. До свидания!")
        break
