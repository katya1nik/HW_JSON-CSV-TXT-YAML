# 1. Работа с файлами JSON
import json


json_string = """
[
    "Иванов Иван Иванович",
    "Петров Петр Петрович"
]
"""

python_data = json.loads(json_string)
print(python_data)

json_string = json.dumps(python_data, ensure_ascii=False, indent=4)
print(json_string)


 #  Создание функции для записи в файл json
def write_json(*data: str, file_path: str, encoding: str = "utf-8") -> None:
    """
    Функция записи в json файл.
    :param data: данные для записи
    :param file_path: путь к файлу (в данном случае название файла)
    :param encoding: кодировка
    """
    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

name1="Никулина Екатерина Александровна"
name2="Иванов Иван Иванович"

write_json(name1, name2, file_path='name.json')

# Создание функции для чтения json

def read_json(file_path: str, encoding: str = "utf-8") -> list[str]:
    """
    Функция чтения json файла.
    :param file_path: путь к файлу (в данном случае название файла)
    :param encoding: кодировка
    """
    with open(file_path, 'r', encoding=encoding) as file:
        return json.load(file)
    
result = read_json("name.json")
print(result)


# Создание функции для дозаписи в файл JSON:

def append_json(file_path: str, *data: str, indent: int = 4, encoding: str = 'utf-8') -> None:
    """
    Функция дозаписи в json файл.
    :param file_path: путь к файлу (в данном случае название файла)
    :param data: данные для записи
    :param indent: отступ
    :param encoding: кодировка
    """
    with open(file_path, 'r', encoding=encoding) as file:
        python_data = json.load(file)


 # Проверка типа данных
    if not isinstance(python_data, list):
        raise TypeError("Поддерживается только добавление в JSON-массив")

    python_data.extend(data)

    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(python_data, file, ensure_ascii=False, indent=indent)

file = 'name.json'
append_json(file, 'Новое имя 25', 'Новое имя 26', indent=2)
