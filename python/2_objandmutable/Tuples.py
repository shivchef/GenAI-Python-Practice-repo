library = ("Books", "Magazines", "newspapers")
#we can allocate variables to these values by using tuples again 
#beware about the values how much and what type is going in.
(item1,item2,item3) = library
print(f"Library consists {item1},{item2},{item3}")
print(f"Library consists {library}")
#we can also wirte / decleare varable as side by side using "","" as seperator and it will automatically take it as tuple
vari1,vari2 = 9,1
# We can easily swap their values by 
vari1, vari2 = vari2 , vari1
# Values swaped

# Membership
print(f"Is research papers in library? {'Magazines' in library}")