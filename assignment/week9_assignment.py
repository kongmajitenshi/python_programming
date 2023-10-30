print("")

# 19
def avg_score(scores) : # 1. 딕셔너리 받아옴 2. 모든 키들의 밸류값 꺼냄 3. 모두 합함.
    sum_scores = 0 
    if scores : # 빈 딕셔너리도 None이 아님.
        for value in scores.values() :
            sum_scores += value
        return sum_scores / len(scores)
    else :
        return None
    # if scores :
    #   return sum(scores.values())/len(scores)
    # else :
    #   return None

scores = {"kim":90, "lee":70, "choi":80} #"kim":90, "lee":70, "choi":80

avg = avg_score(scores)
print(f"평균: {avg}")
print("\n\n")

# 20
def get_students(students) :
    stu_list = []
    if students :
        stu_list = list(students.keys())
        # students = ",".join(students)
        # stu_list.append(students)
        return stu_list
    else :
        return stu_list
    

students = get_students(scores)
print(f"명단 : {students}")
print("\n\n")

#21
def add_dict(dict1, name, score) :
    for i in dict1 :
        if name in dict1.keys() :
            return False
        else :
            dict1[name] = score
            return True
        
true_or_false = add_dict(scores, "lee", 100)
if true_or_false :
    print("입력 완료")
else :
    print("동일 학생 있음\n")
print(true_or_false)
print("\n\n")

# 22

def merge_list(list1, list2) :
    new_list1 = list1 + list2
    new_list1.sort()
    # print(new_list1)
    # new_list2 = [ i for i in new_list1 if new_list1[i] != new_list1[i+1] ]
    new_list2 = []
    for i in new_list1 :
        if i not in new_list2 :
            new_list2.append(i)
    
    return new_list2
    # print(new_list2)

print(merge_list([1,2,3,4,5],[1,2,5]))
print(merge_list([0,1,10],[1,2,6,7,8]))

print("\n")

# 23
def search_index(list1, target) :
    # new_list = []
    # for i, v in enumerate(list1) :
    #     if target == v :
    #         new_list.append(i)
    # return new_list
    new_list = [ i for i, v in enumerate(list1) if target == v]
    return new_list
    

print(search_index([35,28,30,29,30], 30))
print(search_index([35,28,30,29,30], 31))
print("")
# 24

def add_list(list1, list2) :
    if len(list2) > len(list1) :
        list_copy = list2
        list2 = list1
        list1 = list_copy
        del list_copy
    # new_list = list1 
    for index in range(len(list2)) :
        list1[index] += list2[index]
    return list1

print(add_list([1,2,3,4], [1,2]))
print(add_list([0,1], [1,2,6,7,8]))
print(add_list([0,1,2,3,4], [1,2,3,4,5,6]))
print("")   
    
'''
리스트1과 2의 같은 인덱스 값 더하기.
>>
리스트1과 2 i번째 밸류값 더하기.
리스트 1을 카피해서 새로운 리스트로 만들기
그 후에 새로운 리스트
'''
