# cat: кошка
# bat: летучая мышь

# ключ : значение

# dictionary = {
#   "cat": "кошка",
#   "bat": "летучая мышь"
# }

# print(dictionary)
# cat = dictionary["cat"]
# print(cat)

countries = {
  "Африка": ["Египет", "Конго", "ЮАР"],
  "Азия": ["Китай", "Таиланд", "Индонезия"]
}

africa = countries["Африка"]
# print(africa)

country_key = input("Введите название страны: ")
if country_key == "Африка":
  print("Страны Африки: ", countries[country_key])
elif country_key == "Азия":
  print("Страны Азии:", countries[country_key])
else:
  print("Такой страны нет в списке")
