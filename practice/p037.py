price = [2000,3000,3500]
num =[]

num.append(int(input("아메리카노 판매 개수 :")))
num.append(int(input("카페라떼 판매 개수 :")))
num.append(int(input("카푸치노 판매 개수 :")))

sales = price[0] * num[0]
sales = sales + price[1] * num[1]
sales = sales + price[2] * num[2]

print(f"총 매출: {sales}원")