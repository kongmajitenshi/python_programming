coffee = 10

while True :
    money = int(input("돈 내놔 : "))

    if money == 300 :
        print("커피줌")
        coffee -= 1
        print(f"남은 커피는 {coffee}개.")
    elif money > 300 :
        print(f"거스름돈{money-300}원 줌. 커피줌.")
        coffee -= 1
        print(f"남은 커피는 {coffee}개.")
    else :
        print("넣은 돈 다시 줌. 커피도 안줌.")
        print(f"남은 커피는 {coffee}개.")
    
    if coffee == 0 :
        print("커피가 다 떨어짐.")
        break