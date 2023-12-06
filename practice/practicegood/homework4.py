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
    
    score_info = file.readlines()
    for score in score_info:
        score = score.strip()
        score = score.split(",")
        # print(score_info)
        # print(score)
    # for i in range(len(score_info)):
        if len(score) == 4:
            name = score[0]
            kor = score[1]
            eng = score[2]
            math = score[3]
            scores.append(Score(name, kor, eng, math))
    # score_info = score_info.strip()
    # score_info = score_info.split(",")
    print(f"기존 등록된 학생은{len(scores)}명 입니다.")

    file.close()


while True:
    with open(full_filename, "a", encoding="utf8") as file:
        select = menu()
        # print(type(scores))
        if select == "1":
            print("이름, 국어점수, 영어점수, 수학점수를 입력하세요.")
            name2 = input("이름을 넣어주세요.(종료시:바로엔터):")
            if name2 == "":
                continue
            kor2 = input("국어 점수:")
            eng2 = input("영어 점수:")
            math2 = input("수학 점수:")
            score = Score(name2, kor2, eng2, math2)
            scores.append(Score(name2, kor2, eng2, math2))
            file.write(score.file_content())
        elif select == "2":
            print("원하는 이름으로 검색하세요. (빈 칸이면 종료)")
            search_name = input("이름:")
            if search_name == "":
                continue
            for score in scores:
                if search_name == score.name:
                    print(f"{score}")
                    break
            else:
                print(f"{search_name}의 정보가 없습니다.")
        elif select == "3":
            print(f"현재 등록되어 있는 {len(scores)}명의 학생의 정보입니다.")
            for i in range(len(scores)):
                print(f"{scores[i]}")
        elif select == "0":
            break

    