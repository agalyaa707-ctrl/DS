edges = [
    (5, "Tower1", "Tower2"),
    (2, "Tower1", "Tower3"),
    (4, "Tower2", "Tower3"),
    (3, "Tower2", "Tower4"),
    (1, "Tower3", "Tower4")
]

edges.sort()
parent = {}

for cost, a, b in edges:
    parent[a] = a
    parent[b] = b

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    parent[find(a)] = find(b)

mst = []
total = 0

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        mst.append((a, b, cost))
        total += cost

print("Mobile Tower Network:")
for edge in mst:
    print(edge)

print("Minimum Cost:", total)