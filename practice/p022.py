# p022.py
a = "give me {0} apples!".format(3)
b = "give me {0} apples!".format("three")
print(a)
print(b)

num = 3
days = "three days"
c = "I ate {} apples, so I sack for {}".format(num,days)
print(c)
c1 = "I ate {1} apples, so I sack for {0}".format(num,days)
print(c1)

d = "I ate {num} apples, so I sack for {days}".format(num = 4, days = "four days")
print(d)