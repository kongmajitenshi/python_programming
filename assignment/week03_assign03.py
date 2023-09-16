money = int(input("투입한 돈: "))
price = int(input("물건의 가격: "))
change = money - price

print("거스름돈:", change)

coin500 = change // 500
print("500 동전 개수:", coin500)
change = change - (coin500 * 500)

coin100 = change // 100
print("100 동전 개수:", coin100)
change = change - (coin100 * 100)

print(change) # 남은 금액이 0이 되었나 확인해보기 위해 넣었습니다