def getInfoByNumber(number):
    lstRed = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    lstBlack = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    sector1 = [x for x in range(1, 13)]
    sector2 = [x for x in range(13, 25)]
    sector3 = [x for x in range(25, 37)]
    line1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
    line2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    line3 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
    info = {"color": "", "value": 0, "evenProperty": "", "range": "", "sector": "", "lines": ""}

    if number in line1:
        info["lines"] = "line1"
    elif number in line2:
        info["lines"] = "line2"
    elif number in line3:
        info["lines"] = "line3"

    if number in sector1:
        info["sector"] = "1-12"
    elif number in sector2:
        info["sector"] = "13-24"
    elif number in sector3:
        info["sector"] = "25-36"


    if number in range(1, 19):
        info["range"] = "1-18"
    else:
        info["range"] = "19-36"

    if number % 2 == 0 and number != 0:
        info["evenProperty"] = "even"
    else:
        info["evenProperty"] = "odd"

    if number in lstRed:
        info["color"] = "red"
    elif number in lstBlack:
        info["color"] = "black"
    else:
        info["color"] = "green"
    info["value"] = number
    return info
import random
def start(userBalance):
    print(f"ваш баланс: {userBalance}")
    randNumb = random.randint(0,36)
    userBet = input("введите ставку: ")

    betList = []



    while userBet != "no":
        userBet = userBet.split()
        if userBet[1].isdigit() and (int(userBet[1]) < 0 or int(userBet[1]) > 36):
            print("вы ставите ставку на числа который нет")
        elif (not userBet[1].isdigit() and userBet[1] not in
              ["red", "black", "green", "even", "odd", "1-18", "19-36", "1-12", "13-24", "25-36", "line1", "line2", "line3"]):
            print("вы ставите на то чего нет")


        elif int(userBet[0]) < userBalance:
            userBalance = userBalance - int(userBet[0])
            betList.append(userBet)
            print(f"у вас списанно {userBet[0]}, ставка сделана")
        else:
            print("у вас не достаточно средств на баланса")

        userBet = input("введите ставку: ")
    info = getInfoByNumber(randNumb)
    print(info)
    print(betList)

    for bet in betList:

        if info["color"] == bet[1]:
            if info["color"] == "green":
                userBalance = userBalance + int(bet[0]) * 36
                print("Вы поставили на число 0, и победили")
                print(f"ваш баланс: {userBalance}")
            else:
                userBalance = userBalance + int(bet[0]) * 2
                print("Вы угадали цвет")
                print(f"ваш баланс: {userBalance}")

        elif info["value"] == bet[1]:
            userBalance = userBalance + int(bet[0]) * 5
            print("Вы угадали число")
            print(f"ваш баланс: {userBalance}")

        elif info["evenProperty"] == bet[1]:
            userBalance = userBalance + int(bet[0]) * 2
            print("Вы угадали четность числа")
        elif info["range"] == bet[1]:
            userBalance = userBalance + int(bet[0]) * 2
            print("Вы range чисел")
        elif info["sector"] == bet[1]:
            userBalance = userBalance + int(bet[0]) * 3
            print("Вы угадали сектор чисел")
        elif info["lines"] == bet[1]:
            userBalance = userBalance + int(bet[0]) * 3
            print("Вы угадали линию чисел чисел")
        else:
            print("Вы не угадали цвет, или число")

    return userBalance

# ПРИМЕР betList = [['1000', 'red'], ['500', 'green'], ['88', '13'], ['45', '12']]
                    # {"color" : "red", value : "12"}
# import random
# randNumb = random.randint(0,36)
# info = getInfoByNumber(randNumb) # получим информацию о нашем числе
# для примера info = {"color" : "red", value : "12"}
# Нужно связать между собой betList и словарь info и найти совпадения!
# допустим у тебя была ставка на "red" -> ['1000', 'red']
# в словаре info есть значение "red" -> ЗНАЧИТ МЫ ВЫЙГРАЛИ
# также в словаре info есть значение "12" -> МЫ ТОЖЕ СТАВИЛИ НА 12 -> ['45', '12']
# значит победили!
# Значения green и значения "13" - в словаре  info нет. - ставки не сыграли