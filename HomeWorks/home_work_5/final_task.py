import random

import telebot
import credentials

token = credentials.BOT_TOKEN

bot = telebot.TeleBot(token)

RANDOM_TASKS = [
    "Проснуться на 30 минут раньше обычного",
    "Сделать утреннюю зарядку",
    "Приготовить полезный завтрак",
    "Почитать книгу по саморазвитию",
    "Составить список дел на день",
    "Выполнить первое дело из списка",
    "Сделать перерыв на отдых",
    "Пообщаться с другом или близким человеком",
    "Послушать аудиокнигу или подкаст",
    "Помедитировать или заняться йогой",
    "Сделать запись в дневнике",
    "Пообедать здоровой пищей",
    "Посмотреть документальный фильм",
    "Сделать короткую прогулку на свежем воздухе",
    "Ответить на электронные письма или сообщения",
    "Позаниматься хобби",
    "Сделать перерыв на отдых",
    "Поговорить с коллегой или руководителем",
    "Сделать запись в блокноте о своих достижениях за день",
    "Поужинать лёгкой пищей",
    "Посмотреть интересный сериал",
    "Сделать короткую растяжку перед сном",
    "Почитать книгу перед сном",
    "Записать свои мысли и чувства в дневник",
    "Поблагодарить прошедший день за всё хорошее",
    "Подумать о своих целях и планах на следующий день",
    "Помечтать о будущем",
    "Сделать глубокий вдох и выдох, расслабиться",
    "Пожелать спокойной ночи себе и окружающим",
    "Заснуть с приятными мыслями"]

HELP = """
/help - Вывести список доступных команд
/todo {Дата (Сегодня/чч.мм.гг) Название задачи} - Добавить задачу в список (название задачи запрашиваем у пользователя)
/show {Дата} - Напечатать все добавленные задачи на выбранную дату
/random - Добавить случайную задачу по саморазвитию на Сегодня
/exit - Завершить запись задач и выйти"""

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
        print("'Challenge accepted!' >" + " Задача: " + task + " добавлена на дату - " + date)


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=["todo"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    if len(task) < 5:
        bot.send_message(message.chat.id, "Длина названия должна быть не менее 5 символов!")
        raise ValueError("The name must be at least 5 characters long!")
    else:
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


@bot.message_handler(commands=["show"])
def show(message):  # message.text = /show <date>
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    # text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "[] " + task + "\n"
    else:
        text = "Задач на эту дату нет!"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["exit"])
def stop(message):
    goodbye = "Спасибо за пользование программой! До встречи! =)"
    bot.send_message(message.chat.id, goodbye)
    bot.stop_polling()


bot.polling(none_stop=True)
