choice = int(input("도형 선택(1사각 2삼각 3원) : "))

while 1 :
    if choice != 1 and 2 and 3 :
        print("잘못된 입력입니다.")
        break

    if choice == 1 :
        x = int(input("가로 입력:"))
        y = int(input("세로 입력:"))
        area = x*y
        print("도형의 넓이 =", area)
        break
    elif choice == 2 :
        x = int(input("밑변 입력:"))
        y = int(input("높이 입력:"))
        area = (x*y)/2
        print("도형의 넓이 =", area)
        break
    elif choice == 3 :
        r = int(input("반지름 입력:"))
        area = 3.14*(r**2)
        print("도형의 넓이 =", area)
        break