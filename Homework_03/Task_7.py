number = int(input("Enter your number"))
result = 1
i = 1

while i != number + 1:
    result = result * i
    i += 1

print(f"Factorial of {number} = {result}")
