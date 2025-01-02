# 1. Работа с файлами JSON
import json


json_string = """
[
    "Иванов Иван Иванович",
    "Петров Петр Петрович"
]
"""

# Преобразование json в список
result = json.loads(json_string)
print(result)
# Преобразование списка в json
result = json.dumps(result)
print(result)












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

name1={"name": "Никулина Екатерина Александровна"}
name2={"name": "Иванов Иван Иванович"}

write_json(name1, name2, file_path='names_1.json')


# Создание функции для дозаписи в файл JSON:
# with open('name.json', 'r', encoding='utf-8') as file:
#     python_data = json.load(file)

# new_name = "Новое имя25"
# python_data.append(new_name)

# with open('name.json', 'w', encoding='utf-8') as file:
#     json.dump(python_data, file, ensure_ascii=False, indent=4)

# def append_json(*data: list[dict], file_path: str, encoding: str = 'utf-8', indent: int) -> None:
#     with open(file_path, 'r', encoding=encoding) as file:
#         data = json.load(file)


# # Проверка типа данных
#     if not isinstance(data, list):
#         raise TypeError("Поддерживается только добавление в JSON-массив")

#     data.extend(data)

#     with open(file_path, 'w', encoding=encoding) as file:
#         json.dump(data, file, ensure_ascii=False, indent=indent)

# file = 'name.json'
# append_json(file, 'Новое имя25', 'Новое имя 6', indent=2)






# def append_json(
#     file_name: str, *data: str, indent: int = 4, encoding: str = "utf-8"
# ) -> None:
#     """
#     Функция для добавления данных в JSON файл. Работает с JSON массивами.
#     :param file_name: Имя файла для записи.
#     :param data: Данные для добавления в файл.
#     :param indent: Отступы для каждого уровня вложенности.
#     :param encoding: Кодировка файла.
#     """
#     with open(file_name, "r", encoding=encoding) as file:
#         python_data = json.load(file)

#     # Если python data не является списком, то вызываем ошибку
#     if not isinstance(python_data, list):
#         raise TypeError("Поддерживается только добавление в JSON массивы")

#     python_data.extend(data)

#     with open(file_name, "w", encoding=encoding) as file:
#         json.dump(python_data, file, ensure_ascii=False, indent=indent)

#         append_json("name.json", "Новое имя25", "Новое имя 6", indent=2)