userBet = input("введите ставку")
betList = []
while userBet != "no":
    userBet = userBet.split()
    betList.append(userBet)
    userBet = input("введите ставку")
print(betList)