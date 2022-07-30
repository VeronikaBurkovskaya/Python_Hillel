number = float(input("Please enter a number"))

range_defualt = tuple(range(10,101,10))
answer = "Yes" if abs(number) in range_defualt else "No"

print(f"Is {number} in the range? {answer}")

