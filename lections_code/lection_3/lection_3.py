import random

HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - завершить запись задач и выйти
random - добавлять случайную задачу на дату Сегодня"""

RANDOM_TASK = "Записаться на курс"
RANDOM_TASKS = ["Записаться на курс", "Сходить в магазин", "Поиграть в хэллдайверс", "Помыть машину"]

tasks = {

}

run = True

def add_todo(date, task):
    if date in tasks:
        # Дата есть в словаре
        # Добавляем в список задачу
        tasks[date].append(task)
    else:
        # Даты в словаре нет
        # Создаём запись с ключом date
        tasks[date] = []
        tasks[date].append(task)
        print("Задача ", task, "добавлена на дату ", date)

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Введите дату для отображения списка задач: ")
        if date in tasks:
            for task in tasks[date]:
                print("- ", task)
        else:
            print("Такой даты нет")
    elif command == "add":
        date = input("Введите дату для добавления задачи: ")
        task = input("Введите название задачи: ")
        add_todo(date, task)
    elif command == "exit":
        print("Спасибо за пользование программой! До встречи! =)")
        break
    elif command == "random":
        task = random.choice(RANDOM_TASKS)
        add_todo("Сегодня", task)
    # elif command == "rando_date":
    #     add_todo(RANDOM_DATE, RANDOM_TASK)
    else:
        print("Неизвестная команда")
        break
