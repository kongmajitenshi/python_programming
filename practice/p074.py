# p074.py
def findname(target, cmplist):
    if target in cmplist:
        return True
    else:
        return False
    
names = ["kim", "lee", "park"]
result1 = findname("lee", names)
# result2 = findname(names, "lee")

print(result1) #result2) # True result2 는 오류남.

def findname(target, cmplist):
    if isinstance(cmplist, list) and isinstance(target, str):
        if target in cmplist:
            return True
    return False

names = ["kim", "lee", "park"]
result1 = findname("lee", names)
result2 = findname(names, "lee")

print(result1, result2) # True, False