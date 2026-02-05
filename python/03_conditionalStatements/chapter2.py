size = input("Enter the cup size to get the price(small/medium/large): ").lower()

if size == "small":
    print(f"{size} cup price is $10")
elif size == "medium":
    print(f"{size} cup price is $15")
elif size == 'large':
    print(f"{size} cup price is $20")
else:
    print(f"Sorry We dont offer tea on this cup size.")
