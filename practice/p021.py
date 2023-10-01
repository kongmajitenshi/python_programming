# p021.py
A = "\"A\" year:%d month:%d day:%d %s temperature %f" % (2021,9,1,"lowest", 20.5)
B = "\"B\" year:%d month:%d day:%d %s temperature %f" % (2021,9,1,"highest", 20.5)
C = "\"C\" year:%d month:%d day:%d %s temperature %.1f" % (2021,9,2,"lowest", 20.5)
print(A)
print(B)
print(C)

s1 = "A%10sZ" % "az" # %숫자s 할 시 숫자만큼의 빈공간 생성. %10s 는 빈공간 10칸 생성 후 뒤 두칸에 az 넣음. 남은 앞 8칸은 공백.
s2 = "A%-10sZ" % "az" # -를 붙여서 앞에 두 칸에 az 들어감. 뒤에 8칸 공백.
print(s1)
print(s2)

f1 = "[%0.5f]" % 3.141592 # 공백 0칸
f2 = "[%10.5f]" % 3.141592 # 공백 10칸 생성 후 5째자리까지
print(f1)
print(f2)