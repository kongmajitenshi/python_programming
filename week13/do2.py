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

# step3
print("step3", "-" * 10)
score3 = sc.Score4("kor", "eng", "math")
print(score3.scores)

# step4
print("step4", "-" * 10)
score4 = sc.Score5(kor=100, eng=100, math=100) # 키워드 매개변수처럼 호출, 앞부분 애들은 알아서 문자열로 key자리에 들어감.
print(score4.scores)

score5 = sc.Score5(kor=100, eng=100)
print(score5.scores)

score6 = sc.Score5()
print(score6.scores)