# week05_05_for.py p.208

list_of_list = [
    [1, 2, 3],
    [3, 4, 5, 7],
    [10, 11],
]

for items in list_of_list : # foreach > for A in B : 형태로 사용. 
    for item in items :
        print(item, end=" ")
    print()

print()

for items in list_of_list :
    print(items)

name = "최지은"
scores = [22,100,30,40]

for ele in name : # for in 이 기본 구조임.
    print(ele, end="")

for score in scores : # scores에서 하나씩 찾아보고 score에 넣음.
    print(score)