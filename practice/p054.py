# p054.py

for i in range(2,10) :
    print(i,end=",")
print("\n", "-"*30)

for i in range(2,10) :
    print(f"구구단 : {i}단")
    for j in range(1,10) :
        print(f"{i}*{j}={i*j}")

data = [ [1,2,3,], [4,5,6], [7,8,9] ]

for i in range(len(data)) :
    for j in range(len(data[i])) :
        print(data[i][j], end="   ")
print()

