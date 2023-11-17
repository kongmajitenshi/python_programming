# week12_var_01.py

a = 1
b = 1
c = 1

def vartest1(a):
    a = a + 1


def vartest2(b):
    b = b + 1
    return b


def vartest3(): # 다이렉트로 전역변수 바꾸는 코드
    global c # 전역변수 c를 여기서도 쓰겠다~
    c = c + 1


vartest1(a)
b = vartest2(b)
vartest3()

print(a,b,c)
# 1, 2, 2