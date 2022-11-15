import os
import pathlib
import csv


class Client(object):
    def __init__(self, database_path, features):
        self.database_path = database_path
        self.features = features

    def show(self):
        with open(self.database_path, 'r', newline='') as file:
            reader = csv.DictReader(file, fieldnames=[*self.features.keys()], delimiter=';')
            i = 0
            for row in reader:
                print(f"Запись №{i}")
                for key, value in row.items():
                    print(f"{self.features[key]} - {value}")
                print('===============')
                i += 1

    def add(self):
        print("Создание новой записи. Для выхода введите '+'")
        new_car = {}
        for item in (self.features.items()):
            param = ""
            while param == "":
                param = input(f"Введите {item[1]} - ")
            if param == "+":
                break
            new_car[item[0]] = param
        if len(new_car) == len(self.features.items()):
            with open(self.database_path, 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=[*self.features.keys()], delimiter=';')
                writer.writerow(new_car)
            print("Запись добавлена.")

    def change(self):
        with open(self.database_path, 'r', newline='') as file:
            reader = csv.DictReader(file, fieldnames=[*self.features.keys()], delimiter=';')
            cars = list(reader)
            i = 0
            for row in cars:
                print(f"Запись №{i}")
                for key, value in row.items():
                    print(f"{self.features[key]} - {value}")
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
                car_change[key] = input(f"{self.features[key]} - {value}: ") or value
            cars[number] = car_change
            with open(self.database_path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=[*self.features.keys()], delimiter=';')
                writer.writerows(cars)
            print("Измененная запись сохранена")

    def delete(self):
        with open(self.database_path, 'r', newline='') as file:
            reader = csv.DictReader(file, fieldnames=[*self.features.keys()], delimiter=';')
            cars = list(reader)
            i = 0
            for row in cars:
                print(f"Запись №{i}")
                for key, value in row.items():
                    print(f"{self.features[key]} - {value}")
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
            with open(self.database_path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=[*self.features.keys()], delimiter=';')
                writer.writerows(cars)
            print("Запись удалена")


client = Client(
    features={"color": "Цвет", "model": "Модель", "engine volume": "Объем двигателя", "gear box": 'КПП',
              "state": "Состояние",
              "lights": "Фары", "doors": "Двери"},
    database_path=pathlib.Path("database.csv")
)

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
    if (choice == 1):
        client.show()
    elif (choice == 2):
        client.add()
    elif (choice == 3):
        client.change()
    elif (choice == 4):
        client.delete()
    elif (choice == 0):
        exit()
    input()
