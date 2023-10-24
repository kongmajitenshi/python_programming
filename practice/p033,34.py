# p033.py

a = [1,2,3]
b = [4,5,6]
c = a+b

a.append([4,5,6])
b.extend([4,5,6])
c.insert(7, 7)

print(a)
print(b)
print(c)

# p034.py
print("-"*30)
del a[0] # 1 제거됨.
print(a)

del a[-1] # [4,5,6] 제거됨.
print(a)

del a [:2] # 처음부터 2번째 전까지 => 2,3 제거됨.
print(a)

del a[:] # 전체
print(a)

# del a [15] # out of range. 범위 벗어남.
# print(a)

# p035.py
print("-"*30)
print(b)

pop_b = b.pop()
print(b)
print(f"deleted value by pop() : {pop_b}") # 후입선출. 가장 최근에 들어간 6이 사라짐.

pop_b = b.pop()
print(b)
print(f"deleted value by pop() : {pop_b}") # 5가 사라짐. 최상위 인덱스 제거.

pop_b = b.pop(2) # b.pop(2)로 해도 b의 값 변화됨.
print(b)
print(f"deleted value by pop() : {pop_b}") # 2번 인덱스 제거. 즉, pop(n)일 때 n은 인덱스값.
print("-"*15,"c")

print(c)

c.remove(4)
print(c)

