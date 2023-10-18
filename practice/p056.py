# p056.py

values = [1,2,3,4,5,6,7]
print(values)

result1=[]
for value in values :
    result1.append(value*3)
result2 = [value*3 for value in values]
result3 = [value*3 for value in values if value % 2 == 0]
print(result1)
print(result2)
print(result3)
print("----------")
mx = int(input("최대 수 : "))
values1 = list()
print("values1: ",values1)
values2 = []
print("values2: ",values2)
for value in range(1, mx) : # 1부터 mx 전까지.
    values1.append(value)
print(values1)

values2 = [v for v in range(1,mx)]
print(values2) # 1~mx전까지 추가

values3 = [v**2 for v in range(1,mx)]
print(values3)

values4 = [v**2 for v in range(1,mx) if v % 2 == 0]
print(values4)

