price = {
    '아메리카노' : 2000,
    '카페라떼' : 3000,
    '카푸치노' : 3500
}
num = {
    'ame' : 0,
    'lat' : 0,
    'cap' : 0
}
ame_sell = int(input("americano sales : "))
lat_sell = int(input("latte sales : "))
cat_sell = int(input("capuccino sales : "))

num['ame'] += ame_sell
num['lat'] += lat_sell
num['cap'] += cat_sell

sales_ame = price['아메리카노'] * num['ame']
sales_lat = price['카페라떼'] * num['lat']
sales_cap = price['카푸치노'] * num['cap']

print(f"아메리카노 매출:{sales_ame}")
print(f"카페라떼 매출:{sales_lat}")
print(f"카푸치노 매출:{sales_cap}")
print(f"총 매출 : {sales_ame+sales_lat+sales_cap}")