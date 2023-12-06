import os
from score import Score

def menu():
    print("1. 입력")
    print("2. 검색")
    print("3. 전체 파일 출력")
    print("0. 종료")
    return input(">").strip()

path_name = "c:\\202344018\\practice"
full_filename = path_name + "\\list.txt"

scores = []

if not os.path.exists(path_name):
    os.mkdir(path_name)
elif os.path.exists(full_filename):
    file = open(full_filename, "r")
    
    score_info = file.readline()
    score_info = score_info.strip().split(",")
    if len(score_info) == 4:
        name = score_info[0]
        kor = score_info[1]
        eng = score_info[2]
        math = score_info[3]
        scores.append(Score(name,kor,eng,math))
    print(f"기존 등록된 학생은{len(scores)}명 입니다.")

    file.close()


while True:
    with open(full_filename, "a") as file:
        select = menu()
        print(type(scores))
        if select == "1":
            name2 = input("이름:")
            kor2 = input("국어 점수:")
            eng2 = input("영어 점수:")
            math2 = input("수학 점수:")
            score = Score(name2, kor2, eng2, math2)
            file.write(score.file_content())
            scores.append(Score(name2, kor2, eng2, math2))
        elif select == "2":
            search_name = input("찾고싶은 이름:")
            for i in range(len(scores)):
                if search_name == scores[i]:
                    print(f"이름:{scores[i]}")
                else:
                    print(f"해당 학생을 찾지 못했습니다.")
        elif select == "3":
            print(f"현재 등록된 총 학생 수:{len(scores)}명")
            for i in range(len(scores)):
                print(f"{i+1}번 째 학생 정보:{scores[i]}")
        elif select == "0":
            break

    