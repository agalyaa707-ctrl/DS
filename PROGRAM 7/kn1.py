items = [
    ("Laptop", 60000, 5),
    ("Mobile", 30000, 2),
    ("Printer", 20000, 4),
    ("Camera", 25000, 3)
]

capacity = 8
items.sort(key=lambda x: x[1] / x[2], reverse=True)

value = 0

for name, price, weight in items:
    if capacity >= weight:
        capacity -= weight
        value += price
        print("Loaded:", name)
    else:
        value += price * capacity / weight
        print("Partially Loaded:", name)
        break

print("Maximum Value:", value)