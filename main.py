import random
def guessANumber():
    print("Условие: Загадывается число в диапазоне от 1 до 100. Требуется угадать число.")
    count = 0
    print(" Выберите сложность:\n 1) Легкая (от 1 до 10)\n 2) Средняя (от 1 до 100)\n 3) Сложная (от 1 до 1000)")
    checkup = True
    while checkup:
        difficulty = input().lower()
        if (difficulty == "1" or difficulty == "легкая"):
            checkup = False
            difficulty = 10
        elif (difficulty == "2" or difficulty == "средняя"):
            checkup = False
            difficulty = 100
        elif (difficulty == "3" or difficulty == "сложная"):
            checkup = False
            difficulty = 1000
        else: print("Сложность не выбрана, повторите попытку!")

    hiddenNumber = random.randint(1,difficulty)
    print('Введите ваш выбор \033[31m\033[1m{0}\033[0m'.format('[ДЛЯ ЗАВЕРШЕНИЯ ИГРЫ ДОСРОЧНО ВВЕДИТЕ exit]: '))
#   print("\033[34m{}".format(text))
    while (hiddenNumber != 0):

        choise = input()
        if choise.lower() == "exit":
            break
        elif choise.isnumeric() == False:
            print("Вы ввели не число! Повторите выбор!")
        else:
            choise = int(choise)
            count += 1
            if choise == hiddenNumber:
                print('Число угадано! Количество попыток: {0}.'.format(count))
                hiddenNumber = 0
            else:
                if choise > hiddenNumber:
                    print("Загаданное число меньше.")
                else:
                    print("Загаданное число больше.")


def evenOrOdd():
    string = input("Введите строку, разделяя отдельные слова пробелами: ")
    words = string.split()
    even = 0
    odd = 0
    for word in words:
        length = len(word)
        if length % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f"Количество слов четной длины: {even}")
    print(f"Количество слов нечетной длины: {odd}")
def listTask():
    list = []
    print('Введите размерность списка:\n')
    checkUp = True
    while (checkUp):
        N = input()
        if (N.isdigit() and N != "0"):
            checkUp = False
            N = int(N)
        else:
            print("Ошбика ввода! Повторите попытку")
    print('Введите элементы списка:\n')
    for item in range(N):
        checkUp = True
        while (checkUp):
            print(item + 1, "элемент:")
            numeric = input()
            if numeric.isnumeric():
                list.append(int(numeric))
                checkUp = False
            else:
                print("Ошбика ввода! Повторите попытку")

    count = {}
    uniqueElements = []

    for element in list:
        if element in count:
            count[element] += 1
        else:
            count[element] = 1
            uniqueElements.append(element)

    print("Элементы, которые встречаются только один раз:")
    for element in uniqueElements:
        if count[element] == 1:
            print(element)
    zeroCount = 0
    for element in list:
        if element == 0:
            zeroCount += 1
    if zeroCount == 0: print("В списке нету нулевых элементов")
    elif zeroCount == 1: print("В списке всего один нулевой элемент")
    else:
        firstNullElement = list.index(0)
        lastNullElement = len(list) - list[::-1].index(0) - 1
        summary = sum(list[firstNullElement + 1:lastNullElement])
        print(f"Сумма между первым и последним нулевым элементом: {summary}")
def dictionaryTask():
    string = "12345678901234567890"
    dict = {}
    for number in range(10):
        dict[number] = 0
    for symbol in string:
        if symbol.isdigit():
            number = int(symbol)
            dict[number] += 1
    for number, quant in dict.items():
        print(f"{number}: {quant}")
def bakeryTask():
    menu = {
        "торт": {
            "описание": "Торт.",
            "цена": 10,
            "количество": 1000
        },
        "пирожное": {
            "описание": "Пирожное.",
            "цена": 5,
            "количество": 500
        },
        "маффин": {
            "описание": "Маффин.",
            "цена": 4,
            "количество": 450
        },
        "макарон": {
            "описание": "Макарон.",
            "цена": 2,
            "количество": 300
        },
        "мороженое": {
            "описание": "Мороженое.",
            "цена": 1.5,
            "количество": 275
        }
    }

    def printDescription(productName):
        if productName in menu:
            print(f"{productName} - {menu[productName]['описание']}")
        else:
            print("Товар не найден в меню.")

    def printPrice(productName):
        if productName in menu:
            print(f"{productName} - {menu[productName]['цена']} BYN за 100 г")
        else:
            print("Продукт не найден в меню.")

    def printQuantity(productName):
        if productName in menu:
            print(f"{productName} - {menu[productName]['количество']} г")
        else:
            print("Продукт не найден в меню.")

    def printInfo():
        for productName, productInfo in menu.items():
            print(
                f"{productName} - {productInfo['описание']}, {productInfo['цена']} BYN за 100 г, {productInfo['количество']} г")

    def buyProduct(productName, quantity):
        if productName in menu:
            if menu[productName]['количество'] >= quantity:
                totalPrice = (menu[productName]['цена'] * quantity) / 100
                menu[productName]['количество'] -= quantity
                print(f"Покупка успешно завершена. С вас {totalPrice} BYN")
            else:
                print("Недостаточное количество продукта на складе.")
        else:
            print("Продукт не найден в меню.")

    while True:
        print("\nМеню:")
        print("1. Просмотр описания")
        print("2. Просмотр цены")
        print("3. Просмотр количества")
        print("4. Вся информация")
        print("5. Покупка")
        print("6. Выход")

        choice = input("Введите номер пункта меню: ")

        if choice == "1":
            productName = input("Введите название продукции: ").lower()
            printDescription(productName)
        elif choice == "2":
            productName = input("Введите название продукции: ").lower()
            printPrice(productName)
        elif choice == "3":
            productName = input("Введите название продукции: ").lower()
            printQuantity(productName)
        elif choice == "4":
            printInfo()
        elif choice == "5":
            productName = input("Введите название продукции \033[31m\033[1m{0}\033[0m".format("[ДЛЯ ОТМЕНЫ ПОКУПКИ ВВЕДИТЕ CANCEL]: ")).lower()
            if productName.lower() == 'cancel':
                break
            checkup = True
            while(checkup):
                quantity = input("Введите количество (в граммах): ")
                if quantity.isnumeric():
                    checkup = False
                    quantity = int(quantity)
                else: print("Ошибка ввода! Повторите попытку!\n")
            buyProduct(productName, quantity)
        elif choice == "6":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите пункт меню от 1 до 6.")
    return 0
def tupleTask():
    list = []
    print('Введите размерность кортежа:\n')
    checkUp = True
    while (checkUp):
        N = input()
        if (N.isdigit() and N != "0"):
            checkUp = False
            N = int(N)
        else:
            print("Ошбика ввода! Повторите попытку")
    print('Введите элементы кортежа:\n')
    for item in range(N):
        checkUp = True
        while (checkUp):
            print(item + 1, "элемент:")
            numeric = input()
            if numeric.isnumeric():
                list.append(int(numeric))
                checkUp = False
            else :
                print ("Ошбика ввода! Повторите попытку")


    tuple = list
    print("Количество нулевых элементов в кортеже: ",tuple.count(0))

def menu():

    print("   \nВыберите действие: \n"
          "1. Игра \"Угадай число\".\n"
          "2. Подсчитывание слов четной и нечетной длины. \n"
          "3. Задание со списком.\n"
          "4. Задание со словарем.\n"
          "5. Программа \" Кондитерская \"\n"
          "6. Задание с кортежем\n"
          "7. Выйти из программы\n")
    choise = input()
    match choise:
        case "1":
            guessANumber()
            menu()
        case "2":
            evenOrOdd()
            menu()
        case "3":
            listTask()
            menu()
        case "4":
            dictionaryTask()
            menu()
        case "5":
            bakeryTask()
            menu()
        case "6":
            tupleTask()
            menu()
        case "7":
            exit()
        case default:
            print("Неправильный ввод!\n")
            menu()

menu()