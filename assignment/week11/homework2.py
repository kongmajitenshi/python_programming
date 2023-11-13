import os

path_name = "c:\\202344018"
full_filename = path_name + "/list.txt"

if os.path.isfile(full_filename):
    f = open(full_filename, "r")

    scores = []

    while True:
        file = f.readline()
        if not file:
            break

        scores_split = file.split(",")

        if len(scores_split) == 4:
            scores_dict = {"name": None, "kor":None, "eng":None, "mat":None}
            scores_dict['name'] = scores_split[0]
            scores_dict['kor'] = scores_split[1]
            scores_dict['eng'] = scores_split[2]
            scores_dict['mat'] = scores_split[3]
            scores.append(f"이름:{scores_dict['name']} 국어: 영어: 수학:")
            # print(scores_dict) # {'name': '최지은', 'kor': '100', 'eng': '100', 'mat': '100'}
            # print(scores_split) # ['최지은', '100', '100', '100']
            
    f.close()