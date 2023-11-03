# week10_01_param.py

# p.284 위치형 매개변수 positional argument
def info(name, grade) :
    print(f"{name} {grade}")

info("kim", 1)
# info("kim") 값 2개 받아야 하는데 하나만 받아서 에러남.

# p.279 기본(값) 매개변수
def reg(name, grade = 1) :
    print(f"{name} {grade}")

reg("kim",2)
reg("kim")

# 기본값 매개변수 선언은 뒤쪽에 해야함
# def reg(grade = 1, name) :
#     print(f"{name} {grade}")

# reg("kim")


print("장은미", end="\t")
print()
print("1", "2", "3", sep=",", end="\n\n")

# p.280 키워드 매개변수
def intro(name, grade=1, hobby="없음") :
    print(f"이름:{name}")
    print(f"학년:{grade}")
    print(f"취미:{hobby}")

print()
# intro(hobby="디아4", grade=2) # 안된다
intro(hobby="디아4", name="장은미") # 키워드 매개변수는 순서 상관 x 
intro(name="장은미", hobby="디아4")
intro("장은미", hobby="디아4") # 장은미 1 없다
intro("장은미", "없다") # 장은미 없다 없음 출력됨
intro("장은미")

print()
# p.278
# *args 가변인자
def intro(name, grade, *hobbies):
    if 0 < len(hobbies):
        print(hobbies)
    else:
        print(hobbies)

intro("장은미",1, "디아4", "삼국지", "대항해시대")
intro("장은미",1)

print("\n")


def intro(name, *hobbies, grade): # 가변매개변수 뒤의 매개변수는 기본값을 주는게 좋다. 안그럼 자꾸 키워드매개변수 써야해서 귀찮음.
    print(name, grade)
    print(hobbies)

# intro("kim", "lee", "choi", "song")
intro("kim", "lee", "choi", grade="song")

print("\n")
def intro(name, *hobbies, grade="song"): 
    print(name, grade)
    print(hobbies)

intro("kim", "lee", "choi", grade="song")
intro("kim", "lee", "choi", "song")