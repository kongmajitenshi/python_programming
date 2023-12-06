# p110.py
import car

def menu():
    print()
    print("1. 자동차 입고")
    print("2. 자동차 출고")
    print("3. 입고 차량 현황")
    print("0. 종료")
    return input(">").strip()

if __name__ == "__main__":
    car.readfile()

    while True:
        select = menu()
        if select == "1":
            number = input("차량번호:").strip()
            findpos = car.searchnumber(number)
            if findpos == None:
                car_info = car.doin(number)
                print(f"{number}입고 완료")
        elif select == "2":
            number = input("차량번호:").strip()
            findpos = car.searchnumber(number)
            if findpos != None:
                parkingtime, price = car.doout(findpos)
                print(f"{number}출고 완료")
                print(f"    주차 시간:{parkingtime:10}분")
                print(f"    주차요금:{price:10}원")
        elif select == "3":
            car.showcar()
        elif select == "0":
            break