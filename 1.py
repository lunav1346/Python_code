coin500 = 0
coin100 = 0
coin10 = 0

itemPrice = int(input("물건값을 입력하시오?"))
myMoney = int(input("가지고 있는 돈은?"))

change = myMoney - itemPrice

coin500 = change // 500
change = change - (coin500 * 500)

coin100 = change // 100
change = change - (coin500 * 100)

coin10 = change % 100
coin10 = (coin10 / 10)
change = change - (coin500 * 10)

print("거스름돈은 500원=", coin500, "100원=", coin100, "10원=", coin10, "입니다.")