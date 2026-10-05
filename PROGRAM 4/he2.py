import heapq

packets = []

heapq.heappush(packets, (4, "Packet A"))
heapq.heappush(packets, (1, "Packet B"))
heapq.heappush(packets, (2, "Packet C"))

print("Network Packets:", packets)

p = heapq.heappop(packets)

print("Processed:", p[1])
print("Remaining Packets:", packets)