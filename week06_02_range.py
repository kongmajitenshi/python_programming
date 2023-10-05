# week06_02_range.py

# p.234
fruits = ["딸기", "귤", "키위", "복숭아"]

for i in reversed(range(len(fruits))) : # reversed함수 < 뒤집어줌.
    print(f"rank{i+1}: {fruits[i]}")

print("\n\n\n\n");


for i in range(len(fruits)) : # list fruits 의 길이만큼 반복하니 문제가 안생김.
    print(f"rank{i+1}: {fruits[i]}")

print("\n\n\n\n")


for i in range(4) :
    print(f"rank{i+1}: {fruits[i]}")

print("\n\n\n\n")


for fruit in fruits :
    print(fruit)

print("\n\n\n\n")


# p.233
for i in range(0, 100, 1) :
    print("안녕하세요")

print("\n\n\n\n")

for i in [0,1,2,3,4] :
    print("Hello")

print("\n\n\n\n")
# p.230

# range_1 = range(3)
# range_2 = range(0, 3)
# range_3 = range(0, 10, 1)
range_1 = list(range(3))
range_2 = list(range(0, 3))
range_3 = list(range(0, 10, 1))

print(range_1)
print(range_2)
print(range_3)

# range = range(5) # 엄밀히 따지면 '생성자' 임.
# print(range, type(range))
# range = range(3)
# print(range, type(range))
print("\n\n\n\n")