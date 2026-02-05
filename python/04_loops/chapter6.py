boxItems = ["sharpner", "missing", 'scale','exit','pencil']
for boxItem in boxItems:
    if boxItem == "missing":
        continue
    if boxItem == "exit":
        print(f"{boxItem} box exited")
        break

        
print(f"outside loop")