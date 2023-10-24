# p056.py
students = []
titles = ["국", "영", "수"]

number = int(input("인원 : "))

for i in range(number):
    print(f"{i+1}번 학생 >>")
    scores = []
    for title in titles :
        score = input(f"{title} 과목 :")
        scores.append(int(score))
    students.append(scores)
print(students)
print("-----")
# for i, scores in enumerate(students) :
#     print(f"{i+1}번 학생: ")
#     print(scores)
#     for j, score in enumerate(scores) :
#         print(f"\t{titles[j]} 점수 : {score}점")
#     print(f"\t평균:{sum(scores)/len(scores)}")

for i in range(len(students)) :
    print(f"{i+1}번 학생")
    print(i)
    for j in range(len(students[i])):
        print(f"{titles[j]} 점수 : {students[i][j]}점")
    print(f"평균:{sum(students[i])/len(students[i])}")
            
            # print(f"{students[j]}")
            # print(f"{titles[k]} 점수: ")
            # print(k)
            # print(f"{titles[k]} 점수 : {students[k]}")
    # print(f"평균:{sum()}")