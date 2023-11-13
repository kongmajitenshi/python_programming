# week11_02_file.py 집가서 with문 써서 해보셈
import os

targetdir = "c:\\test_q"
if not os.path.exists(targetdir): # not 은 없다면? 이라는 의미
    os.mkdir(targetdir)

file = open(targetdir +"\\test02.txt", "w")

scores = {"MATH":90, "KOR":100, "ENG":40}
for k,v in scores.items():
    data = f"{k},{v}\n"
    file.write(data) 

file.close()