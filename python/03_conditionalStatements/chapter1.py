
choice = input("Enter your preferred snack:").lower()
if choice == 'samosa' or choice == 'cookies' :
    print(f"{choice} Order confirmed!\nThank you for your purchase.")
else:
    print(f"Sorry your ordered item is not available")