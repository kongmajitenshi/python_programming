# p051.py
for value in range(10) :
    print(value, end="/")
print()

for v in range(0,10,1):
    print(v, end=",")
print()

for v in range(2,10):
    print(v, end=",")
print()

for v in range(2,10,3):
    print(v, end=",")
print()

rt = range(10)
lt = list(rt)
print(rt)
print(lt)
lt[0] = 11
age = lt[0]
print(age, lt[0])
# rt[0] = 12
# age = rt[0]