queue = []

queue.append("Person A")
queue.append("Person B")
queue.append("Person C")

print("Waiting Queue:", queue)

removed = queue.pop(0)
print("Ticket Given:", removed)

print("Remaining Queue:", queue)