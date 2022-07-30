first = [2,3]
second = [4,2]

move_vertical = (first[0] + 2 == second[0]) or (first[0] - 2 == second[0])
move_horizontal = (first[1] - 1 == second[1]) or (first[1] + 1 == second[1])

if move_horizontal and move_horizontal:
    print("Chess knight moved successfully")
else: print("Chess knight moved failed")

