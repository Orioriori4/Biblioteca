# Сделайте папку dc на диске C для работы программы
with open("C://dc/bibl", "w") as file:
    file.close()
print("Команды:1 Добавить книгу, 3 Удалить все,4 Найти книгу ")
while True:
    Action = input("Что вы хотите сделать")
    if Action == "1":
        file = open("C://dc/bibl", "a")
        name = input("Название книги:")
        nomer = input("Номер книги:")
        year = input("Год выпуска книги:")
        c = f"{name} | {nomer} | {year}"
        file.write(c + "\n")
        print("Добавлена")
        file.close()
    elif Action == "3":
        Warning = input("ТОЧНО???")
        if Warning == "Да":
            file = open("C://dc/bibl", "w")
            file.close()
            print("Все удалено без востановления:)")
        elif Warning == "Нет":
            print("Обидно ну ок")
    elif Action == "4":
        v = input("По названию 1 или номеру 2 или по дате 3?")
        if v == "1":
            name21 = input("Введите название книги")
            file = open("C://dc/bibl", "r")
            name = file.read()
            nomer = file.read()
            year = file.read()
            if name21 in name:
                ca = f"{name} | {nomer} | {year}"
                print(ca, end="")
                file.close()
            else:
                print("Файл не обнаружен")
        elif v == "2":
            nomer21 = input("Введите номер книги")
            file = open("C://dc/bibl", "r")
            name = file.read()
            nomer = file.read()
            year = file.read()
            if nomer21 in nomer:
                ca = f"{name} | {nomer} | {year}"
                print(ca, end="")
                file.close()
            else:
                print("Файл не обнаружен")
        elif v == "3":
            year21 = input("Введите год книги")
            file = open("C://dc/bibl", "r")
            name = file.read()
            nomer = file.read()
            year = file.read()
            if year21 in nomer:
                ca = f"{name} | {nomer} | {year}"
                print(ca, end="")
                file.close()
            else:
                print("Файл не обнаружен")


