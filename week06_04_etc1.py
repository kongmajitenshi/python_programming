# week06_04_etc1.py
# practice question
ip_addr = [127,0,0,1] #"127.0.0.1" 자기한테 보내는 ip. 
ip_addr = [ str(i) for i in ip_addr ]
new_addr = ".".join(ip_addr)
print(new_addr)

# p.257 *리스트내포
array = []
for i in range(0, 20, 2) :
    if i % 4 != 0: # 조건을 i % 4 로만 해도 돌아감.
        array.append(i*i)
print(array)
print("----------")

array = [ i*i for i in range(0,20,2) if i % 4 != 0 ]
print(array)
print("----------")

array = []
for i in range(0, 20, 2) :
    array.append(i*i)
print(array)
print("----------")

array = [ i*i for i in range(0,20,2) ]
print(array)
print("----------")

# p.263 - join()
fruits = ["딸기", "사과", "배"]
print(", ".join(fruits)
    )
my_fav = ""
for f in fruits :
    if(len(my_fav)) > 0 :
        my_fav += ", "
    my_fav += f
print(my_fav)

# p.256
example = { 1:"one", 2:"two", 5:"five"}
for k in example : print(k)
for k in example.keys() : print(k)
for k in example.values() : print(k)
for k, v in example.items() : print(k, v)



# p.254
scores = [100,45,80,0,23]
for i, score in enumerate(scores) : # tuple 타입
    print(f"{i+1}번 째 과목: {score}")

for i, name in enumerate("김대희") :
    print(i, name)

# p.252 
# scores = [100,45,80,0,23]
# print(reversed(scores))
# print(list(reversed(scores))) # reversed는 원본을 바꾸지 않음.
# print(scores)

# rvs = reversed(scores)
# for r in rvs :
#     print("1st:", r)
# for r in rvs :
#     print("2nd:", r)

# p.251
scores = [100,45,80,0,23]

# print(min(scores))
# print(max(scores))
# print(sum(scores))
# print(sum(scores) / len(scores))

# 사용자가 입력한 점수를 가지고 평균 구하는 코드 작성.