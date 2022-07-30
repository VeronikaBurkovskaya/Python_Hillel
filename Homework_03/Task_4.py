list_of_six = tuple(range(100,200,6))
list_of_five = list();

for i in list_of_six:
    if (i % 5 == 0 and i < 150):
        list_of_five.append(i)

print(list_of_five)
