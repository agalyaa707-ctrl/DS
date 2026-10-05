bookings = [
    [105, "Anisha", "Leo", 2],
    [102, "Rajesh", "Avatar", 3],
    [104, "Kamaraj", "Jawan", 1],
    [101, "Anu", "Leo", 4]
]

def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left = [x for x in data[1:] if x[0] < pivot[0]]
    right = [x for x in data[1:] if x[0] >= pivot[0]]

    return quick_sort(left) + [pivot] + quick_sort(right)

bookings = quick_sort(bookings)

print("Bookings Sorted by ID:")
for b in bookings:
    print(b)