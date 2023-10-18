# p052.py
scores = [] # list()

for data in range(1,6,1) :
    scores.append(int(input(f"{data}번: ")))

print("출력1", "*"*50)

number = 0
for score in scores :
    number += 1
    print(f"{number}번 학생 점수:{score}")

print("출력2", "*"*50)

for idx in range(len(scores)) :
    print(f"{idx+1}번 학생 점수:{scores[idx]}")

print("----------")
avg = sum(scores) / len(scores) 
print(type(sum(scores)))
print(type(len(scores)))
print(type(sum(scores)/len(scores) ))

print("총평균: ",avg)
print("최고점수: ",max(scores))
print("최저점수: ",min(scores))