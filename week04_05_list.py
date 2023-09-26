# week04_05_list.py

test = [1,2,3]
test[2] = 4 # [1,2,4]

test.append(5) # [1,2,4,5] append는 끝에 붙음. 다른 함수에서 append가 없다면 add임.
test.append(6) # [1,2,4,5,6] 
test.insert(2,3) # [1,2,3,4,5,6]
test.insert(0,0) # [0,1,2,3,4,5,6]
test.insert(-20,-1) # [-1,0,1,...,6]
test.insert(20,22) # [-1,0,1,...,6,22]

test = [-1,0,1,2,3,4,5,6,22]

del test[0] # del은 명령어임. [0,1,2,3,4,5,6,22]
del test[3:6] # del은 인덱싱 슬라이싱 모두 가능. > [0,1,2,6,22]

a = test.pop() # 22가 뽑혀서 나감. [0,1,2,6] 변수를 붙인다면 뭐가 빠졌는지 확인 가능. 즉, 사라지지 않음.
b = test.pop(0) # [1,2,6] 0번인덱스가 뽑혀나감. 

test.remove(6) # [1,2] 6이 의미하는 것은 인덱스가 아님. 값을 의미함.




# test = "abc"
# "abc".insert(0,"q") # 문자열은 값 수정x = insert 구현 안됨.

# test.replace("a", "q") # qbc라는 문자열을 새로 생성함. 새로운 변수로 지정해주어야함
# # print(test) # abc가 나옴. 


print(test + [5,6])
print(test * 2)
 