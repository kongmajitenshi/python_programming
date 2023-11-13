import os

path_name = "c:\\202344018"
full_filename = path_name + "/list.txt"

if not os.path.isdir(path_name):
    os.mkdir(path_name)

f = open(full_filename, "a")

while True:
    name = input("이름 입력(바로 Enter 누를 시 종료):")
    if name == None:
        break
    kor = input("국어 점수:")
    eng = input("영어 점수:")
    math = input("수학 점수:")

    f.write(name)
    f.write(kor)
    f.write(eng)
    f.write(math)
f.close()