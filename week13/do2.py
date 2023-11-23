# week13\do2.py
import score as sc
# step1
print("step1", "-" * 10)
score1 = sc.Score1()
print(score1)
print(score1.kor)
print(score1.eng)
print(score1.math)

# step2
print("step2", "-" * 10)
score2 = sc.Score3(10, 20, 30)
print(score2)
print(score2.scores["kor"])

del score2.scores["kor"]
del score2.scores["eng"]
del score2.scores["math"]
print(score2)