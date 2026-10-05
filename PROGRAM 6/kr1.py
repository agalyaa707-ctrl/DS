edges = [
    (4, 'Chennai', 'Salem'),
    (2, 'Chennai', 'Vellore'),
    (5, 'Salem', 'Trichy'),
    (3, 'Vellore', 'Salem'),
    (6, 'Vellore', 'Trichy')
]

edges.sort()
parent = {}

def find(city):
    if parent[city] != city:
        parent[city] = find(parent[city])
    return parent[city]

def union(a, b):
    parent[find(a)] = find(b)

for edge in edges:
    parent[edge[1]] = edge[1]
    parent[edge[2]] = edge[2]

mst = []
total = 0

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        mst.append((a, b, cost))
        total += cost

print("Railway Connections:")
for edge in mst:
    print(edge)

print("Minimum Railway Cost:", total)