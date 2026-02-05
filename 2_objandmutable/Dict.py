box = dict(campass = 1 , divider = 1 , otherItems = "Pencil")
print(f"Content of the box  : {box}")

box2 = {}
box2 ["protractor"] = 1
box2 ["eraser"] = 1
box2 ["sharpner"] = 1

print(f"content of second box : {box2}")

del box["otherItems"]

print(f"new data of box 1:{box}")
#to check membership use 'in' keyword with list disctionary or array

    # print(f"Is sharpner in the box? {'sharpner' in box2}")
    # print(f"all keys of box1 : {box.keys()}")
    # print(f"all values of box1 : {box.values()}")

last_item = box2.popitem()
print(f"Removed last item : {last_item}")

box.update(box2)
print(f"Box final content: {box}")