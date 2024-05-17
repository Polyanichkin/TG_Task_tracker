import random

import telebot
import credentials

token = credentials.BOT_TOKEN

bot = telebot.TeleBot(token)

RANDOM_TASKS = ["Записаться на курс", "Сходить в магазин", "Поиграть в хэллдайверс", "Помыть машину"]

HELP = """
/help - Вывести список доступных команд
/add - Добавить задачу в список (название задачи запрашиваем у пользователя)
/show - Напечатать все добавленные задачи
/exit - Завершить запись задач и выйти
/random - Добавить случайную задачу на дату Сегодня"""

tasks = {}


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


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=["add", "todo"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = "'Challenge accepted!' >" + " Задача: " + task + " добавлена на дату - " + date
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["random"])
def random_add(message):
    date = "сегодня"
    task = random.choice(RANDOM_TASKS)
    add_todo(date, task)
    text = "'Challenge accepted!' >" + " Задача: " + task + " добавлена на дату - " + date
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["show", "print"])
def show(message):  # message.text = /show <date>
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    # text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "[]" + task + "\n"
    else:
        text = "Задач на эту дату нет!"
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)


# Библиотека https://github.com/eternnoir/pyTelegramBotAPI (telebot) позволяет создавать более сложную логику для ботов.
#
# Например, на этом занятии мы использовали команды. Кроме этого в библиотеке доступны следующие фильтры:
# content_types - вид сообщения (текст, аудио и т.д.)
# commands - список команд
# regexp - регулярное выражение
# func - произвольная функция, возвращающая True или False
#
# Более подробно - https://github.com/eternnoir/pyTelegramBotAPI#message-handlers
#
# Также с помощью этой библиотеки можно отправлять не только текст, но и аудио, видео и даже стикеры.
