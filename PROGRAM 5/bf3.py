flights = {
    "Chennai": ["Delhi", "Mumbai"],
    "Delhi": ["Kolkata"],
    "Mumbai": ["Bangalore"],
    "Kolkata": [],
    "Bangalore": []
}

def bfs(start):
    visited = []
    queue = [start]

    while queue:
        city = queue.pop(0)

        if city not in visited:
            visited.append(city)
            queue.extend(flights[city])

    return visited

def dfs(city, visited):
    if city not in visited:
        visited.append(city)

        for next_city in flights[city]:
            dfs(next_city, visited)

print("BFS:", bfs("Chennai"))

visited = []
dfs("Chennai", visited)
print("DFS:", visited)