plates = []

plates.append("Plate 1")
plates.append("Plate 2")
plates.append("Plate 3")

print("Plates:", plates)
print("Top Plate:", plates[-1])

used = plates.pop()
print("Used Plate:", used)

print("Remaining Plates:", plates)