# 1. Работа с файлами JSON
import json


json_string = """
[
    "Иванов Иван Иванович",
    "Петров Петр Петрович"
]
"""

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


# Создание функции для записи в файл json
def write_json(*data: dict, file_path: str, encoding: str = "utf-8") -> None:
    """
    Функция записи в json файл.
    :param data: данные для записи
    :param file_path: путь к файлу (в данном случае название файла)
    :param encoding: кодировка
    """
    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
# Создание функции для записи в файл json
def write_json(*data: dict, file_path: str, encoding: str = "utf-8") -> None:
    """
    Функция записи в json файл.
    :param data: данные для записи
    :param file_path: путь к файлу (в данном случае название файла)
    :param encoding: кодировка
    """
    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Создание функции для записи в файл json
def write_json(*data: dict, file_path: str, encoding: str = "utf-8") -> None:
    """
    Функция записи в json файл.
    :param data: данные для записи
    :param file_path: путь к файлу (в данном случае название файла)
    :param encoding: кодировка
    """
    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

name1={"name": "Никулина Екатерина Александровна"}
name2={"name": "Иванов Иван Иванович"}

write_json(name1, name2, file_path='names_1.json')


# дозапись в файл
# with open('name.json', 'r', encoding='utf-8') as file:
#     python_data = json.load(file)

# new_name = "Новое имя"
# python_data.append(new_name)

# with open('name.json', 'w', encoding='utf-8') as file:
#     json.dump(python_data, file, ensure_ascii=False, indent=4)

# def append_json(file_name: str, *data: str, indent: int = 4, encoding: str = 'utf-8') -> None:
#     with open(file_name, 'r', encoding=encoding) as file:
#         python_data = json.load(file)

# # Проверка типа данных
#     if not isinstance(python_data, list):
#         raise TypeError("Поддерживается только добавление в JSON-массив")

#     python_data.extend(data)

#     with open(file_name, 'w', encoding=encoding) as file:
#         json.dump(python_data, file, ensure_ascii=False, indent=indent)

# file = 'name.json'
# append_json(file, 'Новое имя 1', 'Новое имя 2', indent=2)