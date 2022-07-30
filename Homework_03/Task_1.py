number = input("Enter your number")
result = 0

for index in number:
    result += int(index)

print(f"Sum of digits in the number = {result}")
