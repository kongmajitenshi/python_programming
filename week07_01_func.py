# week07_01_func.py

def test() :
    print("1")
    print("2")

print(test()) # None

def test():
    print(3)
    print(4)
    return 0

print(test()) # 0


def test() :
    print(5)
    return # 값을 반환하기만 하는 역할이 아님. 복귀 혹은 돌아감 혹은 귀환 등의 의미.
    print(6)

print(test())

def test(i) :
    print("Hello\n" * i)
   
test(30)

def test(i) :
    print("Hello\n" * i)
   
test(7) 

def test(i, data) : # 매개변수, parameter
    print(f"{data}\n" * i)
   
test(7, "안녕") # 인자, argument

def avg(s):
    if type(s) is list :
        return sum(s) / len(s)
    elif type(s) is dict:
        s_dict = list(s.values())
        return sum(s_dict) / len(s_dict)
    
    
scores_2 = { "kim":20, "park":30, "choi":40 } 
scores=[100,20,30,40]

print(avg(scores))
print(avg(scores_2))

print(avg("1234"))


def remove_value(src_list, target) :
    return [ i for i in src_list if i != target ]
    # src_list = src_list[:]
    # while target in src_list :
    #     src_list.remove(target)
    # return src_list
    
num = [1,2,2,2,3]
del_num = 2
new_num = remove_value(num, del_num)
print(num)
print(del_num)
print(new_num)

