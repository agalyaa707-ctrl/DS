bookings = [
    ["Akilan", "jananayagan", 250],
    ["guna", "kuu", 180],
    ["nila", "Dc", 220],
    ["lavanya", "Leo", 150]
]

def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left = [x for x in data[1:] if x[2] < pivot[2]]
    right = [x for x in data[1:] if x[2] >= pivot[2]]

    return quick_sort(left) + [pivot] + quick_sort(right)

bookings = quick_sort(bookings)

print("Bookings Sorted by Price:")
for b in bookings:
    print(b)