import random
randNumb = random.randint(0, 37)
redNumbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
blackNumbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
greenNumb = 0


def inputBet(balance):
    userBet = int(input("Добро пожаловать в рулетку, сколько вы бы хотели поставить? "))




def start(userBalance):
    userBet = input("У вас есть возможность поставить ставку, на какой цвет вы хотите поставить? ")
    userBetNumb = input("На какое число вы хотите поставить ставку? ")
    betList = []
    betNumbList = []
    while userBet != "no":
        userBet = userBet.split()
        betList.append(userBet)
        betNumbList.append(userBetNumb)
        userBet = input("У вас есть возможность поставить ставку, на какой цвет вы хотите поставить? ")
        userBetNumb = input("На какое число вы хотите поставить ставку? ")

    if randNumb in redNumbers:
        print(f"Выпало число: {randNumb}, красного цвета")
        if userBet[1] == "red":
            userBalance = userBalance + int(userBet[0])
            print(f"Вы выиграли {userBet[0] * 2}")
        else:
            userBalance = userBalance - int(userBet[0])
            print(f"Вы проиграли {userBet[0]}")


        if randNumb in redNumbers:
            if userBet[1] == ["1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36"]:
                userBalance = userBalance + int(userBet[0])
                print(f"Вы выиграли {userBet[0] * 2}")
            else:
                userBalance = userBalance - int(userBet[0])
                print(f"Вы проиграли {userBet[0]}")
            print(betNumbList)




    elif randNumb in blackNumbers:
        print(f"Выпало число: {randNumb}, черного цвета")
        if userBet[1] == "black":
            userBalance = userBalance + int(userBet[0])
            print(f"Вы выиграли {userBet[0] * 2}")
        else:
            userBalance = userBalance - int(userBet[0])
            print(f"Вы проиграли {userBet[0]}")
    elif randNumb == greenNumb:
        print(f"Выпало число: {randNumb}")
        if userBet[1] == "green":
            userBalance = userBalance + int(userBet[0])
            print(f"Вы выиграли {int(userBet[0]) * 36}")
        else:
            userBalance = userBalance - int(userBet[0])
            print(f"Вы проиграли {userBet[0]}")
    return userBalance
print(start(300))