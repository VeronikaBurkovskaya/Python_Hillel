year = int(input("Please enter a year"))

answer = "Yes" if year%400 ==0 or (year%4 == 0 and year%100 !=0) else "No"

print(f"Is {year} leap-year? {answer}")