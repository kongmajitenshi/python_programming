# week05_02_str.py / title() # p.141, title , strip upper lower 중요함 /split()아주 많이씀 
b ="10 20-30 40 50,60" # p.152 도전문제 해봐

print("10" in b)
print("11" in b)
print("12" not in b)


b ="10 20-30 40 50,60"
# c = b.split() line3 line4 같음.
c = b.split(" ")
print(c)

c = b.split("-") # 여기서 나오는 대괄호는 리스트.
print(c)

c = b.split("$") # $가 없으니 하나로 통째로 묶어서 나눔. split()은 타입을 list로 해줌.
print(c)

print("=" * 30)

a = "     hello PYthone!     "
print(a.find('o'))
print(a.find('O')) # 찾지 못하는 경우엔 -1 리턴
print(a.rfind('o'))
print()

print(f"[{a.strip()}]") # 여기 대괄호는 문자열임
print(f"[{a.lstrip()}]")
print(f"[{a.rstrip()}]")
print()


print(a.upper()) # "     HELLO PYTHONE!     "
print(a.lower()) # "     hello pythone!     "
print(a.title()) # "     Hello Pythone!     "
print(a) # "     hello PYthone!     "
print()
