class ChaiUtils:

    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
raw = "water , milk, ,  ginger, honey  "

# obj = ChaiUtils()
# obj.clean_ingredients(raw)


#we can use the clean_ingredients function of the class ChaiUtils by without creating object
cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)