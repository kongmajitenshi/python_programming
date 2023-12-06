# p103.py
import os

filename = "c:\\202344018\\test_recovery.txt"
scores = {}
if os.path.isfile(filename):
    f = open(filename, "r", encoding='utf8')

    while True:
        line = f.readline()
        # print(line, type(line), len(line))
        if not line:
            break

        data = line.strip().split(',')
        
        if len(data) == 2:
            scores[data[0]] = data[1]
    
    f.close()

    print(scores)

else:

    print(filename + "해당 파일이 존재하지 않음")