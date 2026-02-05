listItems = ["Shivam","Nilu"]
print(f"person in the room are {listItems}")
listItems.append("Suraj")
print(f"person in the room are {listItems}")
listItems.remove("Nilu")
print(f"person in the room are {listItems}")

#Some extra functions extend,insert

boxItems = ["pencil","Eraser"]
outsideItems = ["sharpner","charcoal pencil"]
boxItems.extend(outsideItems)
print(f"Items in the box are : {boxItems}")
boxItems.insert(0,"Pen")
print(f"Items in the box are : {boxItems}")
boxItems.copy(outsideItems)
print(f"Items in the box are : {boxItems}")

#Operator overloading


