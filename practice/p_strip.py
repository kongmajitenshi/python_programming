a = "     abcdefga     "
b = "aaaabaaaa"
print(a) 

print(a.strip()) # abcdefga

print(b.strip('a')) # b
print(b.lstrip('a')) # baaaa
print(b.rstrip('a')) # aaaab