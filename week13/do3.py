# week13\do3.py
import score as sc

scores = []
scores.append(sc.Score(kor=20, eng=30, math=40))
scores.append(sc.Score(kor=20, eng=30))
scores.append(sc.Score(kor=20, math=40))
scores.append(sc.Score())
# print(scores[0].scores)
# print(scores[1].scores)
# print(scores[2].scores)
# print(scores[3].scores)
for score in scores:
    # avg = sc.Score.get_average(score)
    avg = score.get_average()
    # avg = sum(score.scores.values()) / len(score.scores)
    print(avg)
    # print(score)
    
print(scores[0].add_subject("kor"))
print(scores[0].scores)

print(scores[0].add_subject("sci"))
print(scores[0].scores)

'''if None == scores[0].scores.get("kor"):
    scores[0].scores["kor"] = 10
print(scores[0].scores["kor"])

if None == scores[0].scores.get("sci"):
    scores[0].scores["sci"] = 10
print(scores[0].scores["sci"])'''