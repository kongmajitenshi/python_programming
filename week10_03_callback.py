# week10_03_callback.py

def call_10_times(func):
    for i in range(10):
        func(i)

def print_hello(i):
    print(f"{i+1} 안녕")


def print_bye(i):
    print(f"{i+1} 꺼져")

call_10_times(print_hello)  
call_10_times(print_bye) 

# p.323 filter() map()
a = ["1", "2", "3"]
# a = [int(i) for i in a]
a = list(map(int, a)) # int는 생성자.
b = sum(a)

print("\n")

def power(num):
    return num+1


a = [1, 2, 3]
a = map(power, a) # a의 모든 요소를 power에 넣겠다. 매핑함수. a를 power 매핑한 결과값 반환.
b = list(a)
print(b)

# l_data = lambda x:x+1 # 매개변수 x에 x+1을 저장하겠다.
a = [1, 2, 3]
a = map(lambda x:x+10, a) 
b = list(a)
print(b)