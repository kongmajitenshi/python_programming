# p023.py
a = "'{0:<10}'", format("hi")
print(a) 
b = "'{0:<10}'".format("hi") # 좌정렬
print(b)
c = "'{0:>10}'".format("hi") # 우정렬
print(c)
d = "'{0:^10}'".format("hi") # 중정렬
print(d)
e = "'{0:=^10}'".format("hi")
print(e)
f = "'{0:!^10}'".format("hi")
print(f)

y = 3.141592
z = 1.23456
s = "{1:0.4f}".format(y, z)
print(s)
