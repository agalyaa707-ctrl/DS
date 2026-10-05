queue = []

queue.append("Customer 1")
queue.append("Customer 2")
queue.append("Customer 3")

print("Queue:", queue)

print("Inserted:", queue[-1])

removed = queue.pop(0)
print("Served:", removed)

print("Queue:", queue)