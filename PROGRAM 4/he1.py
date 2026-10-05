import heapq

processes = []

heapq.heappush(processes, (3, "Process A"))
heapq.heappush(processes, (1, "Process B"))
heapq.heappush(processes, (2, "Process C"))

print("CPU Processes:", processes)

p = heapq.heappop(processes)

print("Executed:", p[1])
print("Remaining:", processes)