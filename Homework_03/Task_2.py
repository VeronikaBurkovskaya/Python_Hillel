number = input("Enter your number")

val_integer, val_fractional = number.split(".")
first_num = int(val_fractional)//10;

print(f"Integer value = {val_integer} "
      +f"\nFractional value = {val_fractional} "
      +f"\nFirst number after point {first_num}")