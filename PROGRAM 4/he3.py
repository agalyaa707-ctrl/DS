import heapq

orders = []

heapq.heappush(orders, (2, "Order 101"))
heapq.heappush(orders, (1, "Order 102"))
heapq.heappush(orders, (3, "Order 103"))

print("Orders:", orders)

order = heapq.heappop(orders)

print("Delivered:", order[1])
print("Remaining Orders:", orders)