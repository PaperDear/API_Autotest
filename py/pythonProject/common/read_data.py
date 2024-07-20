import json

from config import BASE_DIR


def load_data():
    with open(BASE_DIR + "./data/logintest01.json", encoding="utf-8") as f:
        data = json.load(f)
        new_list = []
        for i in data:
            value = tuple(i.values())
            new_list.append(value)
    return new_list


if __name__ == '__main__':
    # hello world
    print("Hello World!")
