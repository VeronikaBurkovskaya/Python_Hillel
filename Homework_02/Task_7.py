number = int(input("Please enter a number"))
star = ''

for i in range(0,number):
    star = star + "*"

print(f"Input number of stars: {number}" +
          f"\n{star}")