first_list = list(range(10,60,10))
second_list = list()

i = len(first_list)
while i > 0:
    second_list.append(first_list[i-1])
    i -= 1

print(first_list)
print(second_list)

