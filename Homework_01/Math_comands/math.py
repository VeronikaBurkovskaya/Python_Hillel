x = int(input("Input first number"))
y = int(input("Input second number"))

print("First number is " + str(x) +
      "\nSecond number is " + str(y)
      + "\nSum of numbers is " + str (x+y)
      + "\nFloor division of numbers is " + str(x//y)
      + "\nRemider from division of numbers is " + str(x - (y*(x//y)))
      + "\nPower for numbers is " + str(x**y))