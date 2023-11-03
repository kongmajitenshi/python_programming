# week10_02_tuple.py
# p.317

t = (10, 20, 30)
a = t[0]
b = t[1:]
print(a, b, list(b))


t = (10, 20, 30)
for i, v in enumerate(t):
    print(i, v)

a = []
b = [1]
c = ()
d = (1, )# vs. int -> (1)
print(type(a), type(b), type(c), type(d))

# p.318
a, b = [10, 20] # 언패킹, 자리에 맞춰서. a=10, b=20
c, d = (10, 20)
print(type(a),type(c))
print(a,b,c,d)

a = 10, 20, 30 # 패킹. 자동으로 튜플 처리.
b = (10, 20, 30)

c, d, e = a
print(a,c,d,e)

# p.320
a, b = 10, 20
b, a = a, b

for a in enumerate([1,2,3]):
    print(a[0], a[1])

print("\n")

for i, v in enumerate([1,2,3]):
    print(i, v)

print("\n")

def divide(n1, n2):
    if n2 != 0: 
        a = n1 // n2
        b = n1 % n2
        return a, b
    # n2==0 일 땐 에러남.
q, r = divide(10, 4)
print(q, r)
q, r = divide(10, 2)
print(q, r)

