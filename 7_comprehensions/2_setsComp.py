# favourite_tools = [
#     "pencil",
#     "pen",
#     "eraser",
#     "sharpner",
#     "set square",
#     "eraser"
# ]

# unique_items = {item for item in favourite_tools}

# print(unique_items)


recipes = {
    "masala chai" : ["ginger","clove","elaichi"],
    "coffee" : ["cappechino", "dalgona", "dark"],
    "healthy chai": ["kaala chai","clove", "dark"]
}

unique_spices = [spices for ingredients in recipes.values() for spices in ingredients]
print(unique_spices)