import os
import pathlib
import csv
import click

features = {"color": "Цвет", "model": "Модель", "engine volume": "Объем двигателя", "gear box": 'КПП',
            "state": "Состояние",
            "lights": "Фары", "doors": "Двери"}
database_path = pathlib.Path("database.csv")
def test1():
    with open(database_path, 'r', newline='') as file:
        reader = csv.DictReader(file, fieldnames=[*features.keys()], delimiter=';')
        i = 0
        for row in reader:
            i += 1
        print(f"Всего записей: {i}")
def test2():
    with open(database_path, 'r', newline='') as file:
        reader = csv.DictReader(file, fieldnames=[*features.keys()], delimiter=';')
        i = 0
        j = 0
        for row in reader:
            for key, value in row.items():
                if (value != None): j += 1
            print(f"Всего строк в {i} записи: {j}")
            j = 0
            i += 1
def test3():
    with open(database_path, 'r', newline='') as file:
        reader = csv.DictReader(file, fieldnames=[*features.keys()], delimiter=';')
        print(f"Открыт файл {database_path}")

def show():
    with open(database_path, 'r', newline='') as file:
        reader = csv.DictReader(file, fieldnames=[*features.keys()], delimiter=';')
        i = 0
        for row in reader:
            print(f"Запись №{i}")
            for key, value in row.items():
                print(f"{features[key]} - {value}")
            print('===============')
            i += 1
def add():
    print("Создание новой записи. Для выхода введите '+'")
    new_car = {}
    for item in (features.items()):
        param = ""
        while param == "":
            param = input(f"Введите {item[1]} - ")
        if param == "+":
            break
        new_car[item[0]] = param
    if len(new_car) == len(features.items()):
        with open(database_path, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=[*features.keys()], delimiter=';')
            writer.writerow(new_car)
        print("Запись добавлена.")
def change():
    with open(database_path, 'r', newline='') as file:
        reader = csv.DictReader(file, fieldnames=[*features.keys()], delimiter=';')
        cars = list(reader)
        i = 0
        for row in cars:
            print(f"Запись №{i}")
            for key, value in row.items():
                print(f"{features[key]} - {value}")
            print('===============')
            i += 1
    try:
        number = int(input("Введите номер записи, которую хотите изменить - "))
    except ValueError:
        print("Вы ввели некорректные данные")
    if (number >= i):
        print("Введенный номер записи не существует")
    else:
        print("Измените необходимые данные")
        car_change = {}
        for key, value in cars[number].items():
            car_change[key] = input(f"{features[key]} - {value}: ") or value
        cars[number] = car_change
        with open(database_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=[*features.keys()], delimiter=';')
            writer.writerows(cars)
        print("Измененная запись сохранена")
def delete():
    with open(database_path, 'r', newline='') as file:
        reader = csv.DictReader(file, fieldnames=[*features.keys()], delimiter=';')
        cars = list(reader)
        i = 0
        for row in cars:
            print(f"Запись №{i}")
            for key, value in row.items():
                print(f"{features[key]} - {value}")
            print('===============')
            i += 1
    try:
        number = int(input("Введите номер записи, которую хотите удалить - "))
    except ValueError:
        print("Вы ввели некорректные данные")
    if (number >= i):
        print("Введенный номер записи не существует")
    else:
        cars.remove(cars[number])
        with open(database_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=[*features.keys()], delimiter=';')
            writer.writerows(cars)
        print("Запись удалена")
while True:
    os.system('cls')
    print("Данная программа может:")
    print("1) Вывести все возможные транспортные средства и их хар-ки")
    print("2) Добавить новую запись")
    print("3) Изменить необходимую запись")
    print("4) Удалить указанную запись")
    print("0) Завершить работу программы")
    try:
        choice = int(input("Введите необходимые пункт - "))
    except ValueError:
        os.system('cls')
        continue
    os.system('cls')
    match (choice):
        case 1:
            show()
            test1()
            test2()
            test3()
        case 2:
            add()
        case 3:
            change()
        case 4:
            delete()
        case 0:
            break
        case _:
            continue
    click.pause()
# изменение 1