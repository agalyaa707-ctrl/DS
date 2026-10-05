queue = []

queue.append("Ravi")
queue.append("Priya")
queue.append("Kumar")

print("Customers:", queue)

served = queue.pop(0)
print("Served Customer:", served)

print("Waiting Customers:", queue)