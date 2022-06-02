"""
Demo list comprehensions
"""

ingredients = ["SPAM", "Spam", "BAcOn", "EggS"]

ingredients_lower = []
for i in ingredients:
    ingredients_lower.append(i.lower())
print(ingredients_lower)

ingredients = [i.lower() for i in ingredients]
print(ingredients)

names = ["jackson johnson", "brewer", "smith", "rogers", "wilson", "jones", "armstrong", "ray", "rich"]
names_capitalized = [n.capitalize() for n in names]
print(names_capitalized)
