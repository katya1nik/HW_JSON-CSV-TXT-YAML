# 1. Работа с файлами JSON
# import json


# json_string = """
# [
#     "Иванов Иван Иванович",
#     "Петров Петр Петрович"
# ]
# """

# python_data = json.loads(json_string)
# print(python_data)

# json_string = json.dumps(python_data, ensure_ascii=False, indent=4)
# print(json_string)


 #  Создание функции для записи в файл json
# def write_json(*data: str, file_path: str, encoding: str = "utf-8") -> None:
#     """
#     Функция записи в json файл.
#     :param data: данные для записи
#     :param file_path: путь к файлу (в данном случ
# ае название файла)
#     :param encoding: кодировка
#     """
#     with open(file_path, 'w', encoding=encoding) as file:
#         json.dump(data, file, ensure_ascii=False, indent=4)

# name1="Никулина Екатерина Александровна"
# name2="Иванов Иван Иванович"

# write_json(name1, name2, file_path='name.json')

# Создание функции для чтения json

# def read_json(file_path: str, encoding: str = "utf-8") -> list[str]:
#     """
#     Функция чтения json файла.
#     :param file_path: путь к файлу (в данном случае название файла)
#     :param encoding: кодировка
#     """
#     with open(file_path, 'r', encoding=encoding) as file:
#         return json.load(file)
    
# result = read_json("name.json")
# print(result)


# Создание функции для дозаписи в файл JSON:

# def append_json(file_path: str, *data: str, indent: int = 4, encoding: str = 'utf-8') -> None:
#     """
#     Функция дозаписи в json файл.
#     :param file_path: путь к файлу (в данном случае название файла)
#     :param data: данные для записи
#     :param indent: отступ
#     :param encoding: кодировка
#     """
#     with open(file_path, 'r', encoding=encoding) as file:
#         python_data = json.load(file)


 # Проверка типа данных
#     if not isinstance(python_data, list):
#         raise TypeError("Поддерживается только добавление в JSON-массив")

#     python_data.extend(data)

#     with open(file_path, 'w', encoding=encoding) as file:
#         json.dump(python_data, file, ensure_ascii=False, indent=indent)

# file = 'name.json'
# append_json(file, 'Новое имя 25', 'Новое имя 26', indent=2)

# 2. Работа с файлами CSV
import csv

# name_list = [

#     ["Иванов", "Иван", "Иванович"],
#     ["Петров", "Петр", "Петрович"],
# ]

# with open("name.csv", "w", encoding="utf-8-sig") as file:
#     writer = csv.writer(file, delimiter=";", lineterminator="\n")
#     writer.writerows(name_list)



# new_name = ["Сидоров", "Сидор", "Сидорович"]

# with open("name.csv", "a", encoding="utf-8-sig") as file:
#     writer = csv.writer(file, delimiter=";", lineterminator="\n")
#     writer.writerow(name_list)

# with open("name.csv", "r", encoding="utf-8-sig") as file:
#     reader = csv.reader(file, delimiter=";")
#     name_list = list(reader)

# print(name_list)


name_dict = [
    {"lastname": "Иванов", "firstname": "Иван", "middlename": "Иванович"},
    {"lastname": "Петров", "firstname": "Петр", "middlename": "Петрович"},    
]

# with open("name.csv", "w", encoding="utf-8-sig") as file:
#     writer = csv.DictWriter(
#         file, fieldnames=name_dict[0].keys(), delimiter=";", lineterminator="\n"
#     )
#     writer.writeheader()
#     writer.writerows(name_dict)


# new = {"lastname": "Пантелеев", "firstname": "Пантелей", "middlename": "Паетелеевич"}

# with open("name.csv", "a", encoding="utf-8-sig") as file:
#     writer = csv.DictWriter(
#         file, fieldnames=name_dict[0].keys(), delimiter=";", lineterminator="\n"
#     )
#     writer.writerow(new)

with open("name.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file, delimiter=";")
    name_dict = list(reader)

from pprint import pprint
pprint(name_dict, sort_dicts=False, width=100)

from tabulate import tabulate
print(tabulate(name_dict, headers="keys", tablefmt="grid"))

html_table = tabulate(name_dict, headers="keys", tablefmt="html")

styled_table = html_table.replace(
    '<table>', 
    '<table class="table table-striped table-hover">'
)

html_template = f"""
<!doctype html>
<html lang="ru">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Список имен</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container mt-5">
            <h1 class="mb-4">Список имен</h1>
            {styled_table}
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    </body>
</html>
"""


with open("name.html", "w", encoding="utf-8") as file:
    file.write(html_template)
