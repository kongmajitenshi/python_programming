# week05_04_list_method.py
# p.205 sort()
a = ["a", "1", 1.1]
print(1 in a)
print("1" in a)
print("A" not in a)
print("a" not in a)
print()

a = [3, 5, 7, 4, 1]
b = a[:] # 리스트 a 복사해서 b라 칭함.

c = sorted(a)
d = sorted(a, reverse=True)
print("c", c)
print("d", d)
print("a", a)

a.sort()
print("a.sort()", a) # asc sorting, 정방향, 오름차순
a.sort(reverse=True) # 역방향.
print("a.sort(reverse=True)",a)
print()

# p.200 ~ 205
a = [1, 2, 3, 4, 5]
print(a)
a.clear() # a 리스트 내용을 삭제. 리스트는 유지. del a[:]와 같은 역할.
print(a)

test_list = [1, 2, 3]
add_list = ["a", "b"]

test_list.extend(add_list)
add_list.extend(test_list)
print(test_list)
print(add_list)
# add_list.extend()

result_list = test_list + add_list
print(test_list + add_list)
print(result_list)
print(test_list)
print(add_list)