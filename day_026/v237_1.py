with open("file1.txt") as f1:
    numbers_list_1 = f1.readlines()

with open("file2.txt") as f2:
    numbers_list_2 = f2.readlines()

result = [int(n) for n in numbers_list_1 if n in numbers_list_2]
