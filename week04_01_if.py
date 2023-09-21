# week04_01_if.py

# 주민등록번호 1111111111111
reg_num = input("주민등록번호")
gen_num = int(reg_num[6])
# 남자인 경우를 출력
# 7 번째. 6번인덱스=7번째 1,3,5,7

# p.171
if 0 < gen_num < 9 and gen_num % 2 == 1:
    print("남자")


if 0 < gen_num < 9:
    if gen_num % 2 == 1:
        print("남자")

# p.170 in
if reg_num[6] in "1357": 
    print("남자")

if str(gen_num) in "1357": # 1357은 문자열, gen_num은 인트형이라 에러남. int("1357")로 묶어도 에러남. gen_num을 str로 변환하면 잘 돌아감. 문제 낼만함.
    print("남자")

# p.160 and?
if gen_num == 1 \
or gen_num == 3 \
or gen_num == 5 \
or gen_num == 7:
    print("남자")

# p.163
number = int(input("정수:"))

if number > 0: 
    print("양수")

if number < 0:
    print("음수")

if number == 0:
    print("0")
