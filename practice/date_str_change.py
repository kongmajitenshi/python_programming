import datetime as dt

d1 = dt.datetime.now()
d2 = dt.datetime.strftime(d1, "%Y-%m-%d %H:%M:%S")
d3 = dt.datetime.strptime(d2, "%Y-%m-%d %H:%M:%S")

print(type(d1), d1)
print(type(d2), d2)
print(type(d3), d3)

