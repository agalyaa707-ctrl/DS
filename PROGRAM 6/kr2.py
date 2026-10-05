edges = [
    (6, 'Tank', 'Block A'),
    (3, 'Tank', 'Block B'),
    (2, 'Block A', 'Block B'),
    (4, 'Block A', 'Block C'),
    (5, 'Block B', 'Block C')
]

edges.sort()
parent = {}

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    parent[find(a)] = find(b)

for cost, a, b in edges:
    parent[a] = a
    parent[b] = b

mst = []
total = 0

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        mst.append((a, b, cost))
        total += cost

print("Pipeline Connections:")
for edge in mst:
    print(edge)

print("Minimum Pipeline Cost:", total)