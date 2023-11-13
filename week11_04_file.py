# week11_04_file.py

scores = [
    ["김인하","2","컴퓨터정보"],
    ["이인하","1","컴퓨터시스템"],
    ["박인하","3","컴퓨터정보"],
]

with open("c:\\test_a\\test03.txt," "w") as file:
    for v in scores:
        w_data = "|".join(v) + "\n"
        file.write(w_data)

# file = open("c:\\test_a\\test03.txt", "w")

# for v in scores:
#     w_data = "|".join(v) + "\n"
#     file.write(w_data)

# file.close()


with open("c:\\test_a\\test03.txt", "r") as file:
    result = []

    for line in file:
        # "김인하|2|컴퓨터정보\n"
        result.append(line.split().split("|"))


# file = open("c:\\test_a\\test03.txt", "r")
# result = []

# for line in file:
#     # "김인하|2|컴퓨터정보\n"
#     result.append(line.split().split("|"))

# file.close()

