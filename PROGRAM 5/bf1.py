graph = {
    "Arun": ["Bala", "Divya"],
    "Bala": ["Arun", "Kumar"],
    "Divya": ["Arun", "Meena"],
    "Kumar": ["Bala"],
    "Meena": ["Divya"]
}

def bfs(start):
    visited = []
    queue = [start]

    while queue:
        person = queue.pop(0)
        if person not in visited:
            visited.append(person)
            queue.extend(graph[person])

    return visited

def dfs(person, visited):
    if person not in visited:
        visited.append(person)
        for friend in graph[person]:
            dfs(friend, visited)

visited = []

print("BFS:", bfs("Arun"))

dfs("Arun", visited)
print("DFS:", visited)