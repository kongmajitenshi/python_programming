# week04_04_list.py
# list = array와 비슷한 역할
# array(배열) > 고정길이, 연속적 메모리 할당

# p.193
stu_1 = [20230001, "김인하", "컴정", 20]
stu_2 = [20230010, "이인하", "컴시", 21]

stu_2[1] = "이하인" # 배열 인덱스 값 변경 하듯이 변경 가능

# stu_1 학생의 입학년도 출력
print(str(stu_1[0])[0:4])

# stu_1 학생의 성(family name)을 출력하세요.
# stu_1[0] > 20230001 나옴 // stu_1[1] > "김인하" 나옴.
print(stu_1[1][0])

#stu_1 학생의 이름(first name)을 출력하세요
print(stu_1[1][1:3])

test_list = ["김인하", 20, 160.5]
print(test_list)

for test in test_list:
    print(test)

test_list = [1,2,3]
print(test_list) # [1,2,3] 으로 출력됨. 대괄호는 리스트다 라는 표현

# p.192
test_list = list() # 생성자
print(test_list, type(test_list))

test_list = [] # 리터럴 형태
print(test_list, type(test_list))