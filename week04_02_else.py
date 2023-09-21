# week04_02_else.py
num = int(input("정수:"))

if num > 0:
    print("양수")
elif num < 0:
    print("음수")
else:
    print("0")
    

if num > 0:
    print("양수")
else :
    if num == 0:
        print("0")
    else :
        print("음수")



# p.177
reg_num = input("주민등록번호:")
gen_num = int(reg_num[6])

if gen_num % 2 == 1:
    print("남자")
else:
    print("여자")