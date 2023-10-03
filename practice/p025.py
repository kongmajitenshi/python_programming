# p025.py
a = "hi"
pi = 3.141592
b = f"|{pi:==12.2f}|" # pi:=12.2f 했을 땐 = 없이 출력됨. 이유는??
left = f"|{'hi':=<10}|"
center = f"|{a:=^10}|"
right = f"|{a:=>10}|"
print("b:", b)
print(left)
print(center)
print(right)

c2 = f"|{a:=^10}|"
r2 = f"|{a:=>10}|"
print(c2)
print(r2)


str_pi = f"{pi:0.2f}"
print(str_pi)

str_pi = f"{pi:10.2f}"
print(str_pi)

str_pi = f"{pi:010.2f}"
print(str_pi)