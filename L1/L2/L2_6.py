# Lesson 2.6

catalog = {}

for i in range(1, 4):
    name = input('Enter the name of a product: ')
    quantity = int(input('Enter the quantity of a product: '))
    catalog[name] = quantity

print(catalog)
print('name:', catalog.keys())
print('quantities:', catalog.values())


