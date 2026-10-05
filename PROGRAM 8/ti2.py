bookings = [
    ["Arun", "Leo", 2],
    ["Bala", "Avatar", 3],
    ["Kumar", "Jawan", 1],
    ["Divya", "Avatar", 4]
]

def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left = [x for x in data[1:] if x[1] < pivot[1]]
    right = [x for x in data[1:] if x[1] >= pivot[1]]

    return quick_sort(left) + [pivot] + quick_sort(right)

bookings = quick_sort(bookings)

print("Bookings Sorted by Movie:")
for b in bookings:
    print(b)