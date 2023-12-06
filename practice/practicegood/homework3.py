import os
from score import Score

path_name = "c:\\202344018\\practice"
full_filename = path_name + "\\list.txt"

if os.path.isfile(full_filename):
    f = open(full_filename, "r")

    scores = []
    # print(f"타입{type(scores)}")
    while True:
        score = f.readline()
        if score == None:
            break

        score = score.split(",")
        if len(score) == 4:
            name = score[0]
            kor = score[1]
            eng = score[2]
            math = score[3]
            scores.append(Score(name, kor, eng, math)) # 리스트의 0번 인덱스에 추가
            # scores = Score(name, kor, eng, math) # scores를 Score타입으로 바꿔버림.
        print(scores[0])
        # print(f"타입{type(scores)}")
        break

    f.close()