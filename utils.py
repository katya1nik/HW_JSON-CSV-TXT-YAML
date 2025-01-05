import json
import csv
import yaml

# JSON
def write_json(*data: str, file_path: str, encoding: str = "utf-8") -> None:
   
    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def read_json(file_path: str, encoding: str = "utf-8") -> list[str]:
    with open(file_path, 'r', encoding=encoding) as file:
        return json.load(file)
    
def append_json(file_path: str, *data: str, indent: int = 4, encoding: str = 'utf-8') -> None:
    with open(file_path, 'r', encoding=encoding) as file:
        python_data = json.load(file)

    if not isinstance(python_data, list):
        raise TypeError("Поддерживается только добавление в JSON-массив")

    python_data.extend(data)

    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(python_data, file, ensure_ascii=False, indent=indent)

# CSV
name_list = [

    ["Иванов", "Иван", "Иванович"],
    ["Петров", "Петр", "Петрович"],
]
def write_csv(data, file_path, delimiter=';', encoding: str ='utf-8-sig') -> None:
    with open(file_path, 'w', encoding=encoding) as file:
        writer = csv.writer(file, delimiter=delimiter, lineterminator="\n")
        writer.writerows(name_list)

def read_csv(file_path, delimiter=';', encoding: str ='utf-8-sig')-> list[str]:

    with open(file_path, 'r', encoding=encoding) as file:
        reader = csv.reader(file, delimiter=delimiter)
        return list(reader)
    

def append_csv(file_path, data, delimiter=';', encoding: str ='utf-8-sig') -> None:
    with open(file_path, 'a', encoding=encoding) as file:
        writer = csv.writer(file, delimiter=delimiter, lineterminator="\n")
        writer.writerow(data)

# TXT
def write_txt(*data: str, file_path, mode: str = "w", encoding: str = "utf-8") -> None:   
    with open(file_path, mode, encoding=encoding) as file:
        for line in data:
            file.write(line + "\n")


def append_txt(*data: str, file_path, mode: str = "a", encoding: str = "utf-8") -> None:
    with open(file_path, mode, encoding=encoding) as file:
        for line in data:
            file.write(line + "\n")


def read_txt(file_path, encoding: str = "utf-8") -> list[str]:
    with open(file_path, encoding=encoding) as file:
        return [line.strip() for line in file.readlines()]
# YAML
def read_yaml(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)
    



