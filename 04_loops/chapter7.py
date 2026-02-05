staff = [("Amit",17),("sohan",22)]

for name,age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff")
        break
else:#fallback logic
    print(f"No one is eligible to managing the staff")