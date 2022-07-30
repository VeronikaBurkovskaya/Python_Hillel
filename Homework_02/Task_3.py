velocity = float(input("Please enter Vasya's velocity"))
time = float(input("Please enter Vasya's time"))

if velocity<0:
    print(f"Vasya rode out of competition {velocity*time} km")
elif velocity*time >100:
    print("Vasya is Flash")
else:
    print(f"Vasya rode a bycicle with velocity {velocity} during {time} hours and passed {velocity*time} km")