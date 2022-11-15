import pickle
import os.path
import os
class Cars:

    def __init__ (self, name, fares = "Выключены", engine = None, color = None, doors = "Закрыты", year = None, developer = None, power = None, price = None):
        self.fares = fares
        self.engine = engine
        self.name = name
        self.color = color
        self.doors = doors
        self.year = year
        self.developer = developer
        self.power = power
        self.price = price

    def __getstate__ (self) -> dict:
        state = {}
        state["fares"] = self.fares
        state["engine"] = self.engine
        state["name"] = self.name
        state["color"] = self.color
        state["doors"] = self.doors
        state["year"] = self.year
        state["developer"] = self.developer
        state["power"] = self.power
        state["price"] = self.price
        return state

    def __setstate__ (self, state: dict):
        self.fares = state["fares"]
        self.engine = state["engine"]
        self.name = state["name"]
        self.color = state["color"]
        self.doors = state["doors"]
        self.year = state["year"]
        self.developer = state["developer"]
        self.power = state["power"]
        self.price = state["price"]
    
    def car_info (self):

        print(f'Модель: {self.name}. Цвет: {self.color}. Год производства: {self.year}. Двигатель: {self.engine}. Фары: {self.fares}. Двери: {self.doors}. Производитель: {self.developer}. Мощность: {self.power}. Стоимость: {self.price}')
        
class Interface:


    def __init__ (self):
        self.GUI()

    def GUI(self):
        while True:
            print("1) Добавить авто")
            print("2) Изменить авто")
            print("3) Удалить авто")
            print("4) Список всех авто")

            choice = input()

            if choice == "1":
                fileSize5 = os.path.getsize("d:/Мои проекты/Лабораторные работы/Основы программной инженерии/Лаб2_Ризамамедов Д.А. (Авто-1)Папка/file.pkl")
                print('Укажите модель:')
                mass.append(Cars(name = input()))
                print('Укажите цвет:')
                mass[len(mass) - 1].color = input()
                print('Укажите год производства:')
                mass[len(mass) - 1].year = input()
                print('Укажите двигатель:')
                mass[len(mass) - 1].engine = input()
                print('Укажите производителя:')
                mass[len(mass) - 1].developer = input()
                print('Укажите мощность:')
                mass[len(mass) - 1].power = input()
                print('Укажите стоимость:')
                mass[len(mass) - 1].price = input()
                with open("file.pkl","wb") as fp:
                    pickle.dump(mass, fp)
                fileSize6 = os.path.getsize("d:/Мои проекты/Лабораторные работы/Основы программной инженерии/Лаб2_Ризамамедов Д.А. (Авто-1)Папка/file.pkl")
                if fileSize6>fileSize5:
                    print("Добавление прошло успешно!")
            elif choice == '2':
                vrizm1 = os.stat("d:/Мои проекты/Лабораторные работы/Основы программной инженерии/Лаб2_Ризамамедов Д.А. (Авто-1)Папка/file.pkl").st_mtime
                fileSize3 = os.path.getsize("d:/Мои проекты/Лабораторные работы/Основы программной инженерии/Лаб2_Ризамамедов Д.А. (Авто-1)Папка/file.pkl")
                for i in range(len(mass)):
                        print(i+1,') ',mass[i].name,' (',"Цвет: ", mass[i].color,', ',"Год: ", mass[i].year,', ',"Двигатель: ", mass[i].engine,', ',"Производитель: ", mass[i].developer,', ',"Мощность: ", mass[i].power,', ',"Стоимость: ", mass[i].price,', ',"Двери: ",mass[i].doors,', ',"Фары: ",mass[i].fares,')', sep = '')
                print("Укажите номер авто, которое хотите изменить:")
                i = int(input())-1
                if i not in [x for x in range(1,len(mass))]:
                    print('Введите корректное значение!')
                else:
                    print('1) Изменить модель')
                    print('2) Изменить цвет')
                    print('3) Изменить год производства')
                    print('4) Изменить двигатель')
                    print('5) Изменить производителя')
                    print('6) Изменить мощность')
                    print('7) Изменить стоимость')
                    print('8) Открыть/закрыть двери')
                    print('9) Включить/выключить фары')
                    print('0) Вернуться')
                    choice2 = input()
                    if choice2 == '1':
                        print('Введите изменённую модель:')
                        mass[i].model = input()
                        with open("file.pkl","wb") as fp:
                            pickle.dump(mass, fp)
                    if choice2 == '2':
                        print('Введите изменённый цвет:')
                        mass[i].color = input()
                        with open("file.pkl","wb") as fp:
                            pickle.dump(mass, fp)
                    if choice2 == '3':
                        print('Введите изменённый год производства:')
                        mass[i].year = input()
                        with open("file.pkl","wb") as fp:
                            pickle.dump(mass, fp)
                    if choice2 == '4':
                        print('Введите изменённый двигатель:')
                        mass[i].engine = input()
                        with open("file.pkl","wb") as fp:
                            pickle.dump(mass, fp)
                    if choice2 == '5':
                        print('Введите изменённого производителя:')
                        mass[i].developer = input()
                        with open("file.pkl","wb") as fp:
                            pickle.dump(mass, fp)
                    if choice2 == '6':
                        print('Введите изменённую мощность:')
                        mass[i].power = input()
                        with open("file.pkl","wb") as fp:
                            pickle.dump(mass, fp)
                    if choice2 == '7':
                        print('Введите изменённую стоимость:')
                        mass[i].price = input()
                        with open("file.pkl","wb") as fp:
                            pickle.dump(mass, fp)
                    if choice2 == '8':
                        choice3 = ''
                        while choice3 != '0':
                            print('1) Открыть')
                            print('2) Закрыть')
                            print('0) Назад')
                            choice3 = input()
                            if choice3 != '1' or '2' or '0':
                                print('Введите корректное значение!')
                            else:
                                if choice3 == '1':
                                    mass[i].doors = "Открыты"
                                    with open("file.pkl","wb") as fp:
                                        pickle.dump(mass, fp)
                                if choice3 == '2':
                                    mass[i].doors = "Закрыты"
                                    with open("file.pkl","wb") as fp:
                                        pickle.dump(mass, fp)

                    if choice2 == '9':
                        choice3 = ''
                        while choice3 != '0':
                            print('1) Включить')
                            print('2) Выключить')
                            print('0) Назад')
                            choice3 = input()
                            if choice3 != '1' or '2' or '0':
                                print('Введите корректное значение!')
                            else:
                                if choice3 == '1':
                                    mass[i].fares = "Включены"
                                    with open("file.pkl","wb") as fp:
                                        pickle.dump(mass, fp)
                                if choice3 == '2':
                                    mass[i].fares = "Выключены"
                                    with open("file.pkl","wb") as fp:
                                        pickle.dump(mass, fp)

                    if choice2 == '0':
                        choice = Interface()
                    
                    if choice2 not in ['1','2','3','4','5','6','7','8','9','0']:
                        print('Введите корректное значение!')
                    print(vrizm1)
                    vrizm2 = os.stat("d:/Мои проекты/Лабораторные работы/Основы программной инженерии/Лаб2_Ризамамедов Д.А. (Авто-1)Папка/file.pkl").st_mtime
                    print(vrizm2)
                    fileSize4 = os.path.getsize("d:/Мои проекты/Лабораторные работы/Основы программной инженерии/Лаб2_Ризамамедов Д.А. (Авто-1)Папка/file.pkl")
                    if fileSize4!=fileSize3 and vrizm1!=vrizm2:
                        print("Изменение прошло успешно!")
                        
                                
            elif choice == '3':
                fileSize1 = os.path.getsize("d:/Мои проекты/Лабораторные работы/Основы программной инженерии/Лаб2_Ризамамедов Д.А. (Авто-1)Папка/file.pkl")
                if len(mass) == 0:
                    print('Нет авто')

                else:
                    for i in range(len(mass)):
                        print(i+1,') ',mass[i].name,' (',"Цвет: ", mass[i].color,', ',"Год: ", mass[i].year,', ',"Двигатель: ", mass[i].engine,', ',"Производитель: ", mass[i].developer,', ',"Мощность: ", mass[i].power,', ',"Стоимость: ", mass[i].price,', ',"Двери: ",mass[i].doors,', ',"Фары: ",mass[i].fares,')', sep = '')
                    choice3 = int(input())
                    if choice3 not in [x for x in range(0,len(mass)+1)]:
                        print('Введите корректное значение!')
                    else: del mass[i-1]
                    with open("file.pkl","wb") as fp:
                        pickle.dump(mass, fp)
                fileSize2 = os.path.getsize("d:/Мои проекты/Лабораторные работы/Основы программной инженерии/Лаб2_Ризамамедов Д.А. (Авто-1)Папка/file.pkl")
                if fileSize1>fileSize2:
                    print("Удаление прошло успешно!")
            elif choice == '4':
                if len(mass) == 0:
                    print('Нет авто')
                else:
                    for i in range(len(mass)):
                        print(i+1,') ',mass[i].name,' (',"Цвет: ", mass[i].color,', ',"Год: ", mass[i].year,', ',"Двигатель: ", mass[i].engine,', ',"Производитель: ", mass[i].developer,', ',"Мощность: ", mass[i].power,', ',"Стоимость: ", mass[i].price,', ',"Двери: ",mass[i].doors,', ',"Фары: ",mass[i].fares,')', sep = '')
                input()

            else:
                
                print("Введите корректное значение!")
                choice = Interface()
mass=[]
with open("file.pkl","rb") as fp:
    mass = pickle.load(fp)
choice = Interface()
