import os

path_name = "c:\\202344018"
full_filename = path_name + "/list.txt"

if os.path.isfile(full_filename):
    f = open(full_filename, "r")

    scores = []

    while True:
        line = f.readline()

        if not line:
            break

        line = line.strip()

        split_line = line.split(",")

        if len(split_line) == 4:
            scores_dict = {"name": None, "kor":None, "eng":None, "mat":None}
            scores_dict['name'] = split_line[0]
            scores_dict['kor'] = split_line[1]
            scores_dict['eng'] = split_line[2]
            scores_dict['mat'] = split_line[3]
            scores.append(f"이름:{scores_dict['name']} 국어:{scores_dict['kor']} 영어:{scores_dict['eng']} 수학:{scores_dict['mat']} 평균:{((int(scores_dict['kor'])+int(scores_dict['eng'])+int(scores_dict['mat'])))/(len(scores_dict)-1)}")

    for score in scores:
        print(score)
            
            
    f.close()