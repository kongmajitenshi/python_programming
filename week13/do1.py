# week13\do1.py
import student as st # 이 땐 st.~~~으로 사용.
from student import Student1 # 바로 class에 접근 가능.

# step1
print("step1", "-" * 10)
stu1 = Student1()

# step2
print("step2", "-" * 10)
stu2 = st.Student2()
print(stu2)
# print(stu2.name) # AttributeError: 'Student2' object has no attribute 'name'

# step3
print("step3", "-" * 10)
stu3 = st.Student3() # object = 객체. 조금 더 고급지게 instance라 부름.
stu4 = st.Student3()
print(stu3)
print(stu4)
stu3.name = "kiminha"
stu4.name = "parkinha"
print(stu3.name)
print(stu3.number)
print(stu3.major)
print(stu4.name)

# step4
print("step4", "-" * 10)
# stu4 = st.Student4()
# print(stu4)
stu4 = st.Student4("김대희", "202344018", "컴정")
print(stu4)
print(stu4.name)
print(stu4.number)
print(stu4.major)

stu5 = st.Student4("김대희", "202344018", )
print(stu5)
print(stu5.name)
print(stu5.number)
print(stu5.major)

# step5
print("step5", "-" * 10)

stu_list = []

while True:
    number = input("number:")
    name = input("name:")
    major = input("major:")

    stu_list.append(st.Student4(name, number, major))

    if "Y" != input("계속?(Y)").upper() :
        break


for stu in stu_list:
    print(stu)