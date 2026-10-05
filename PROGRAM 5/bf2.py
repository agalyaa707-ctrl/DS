cities = ["Chennai", "Vellore", "Salem", "Trichy"]

graph = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

def bfs(start):
    visited = [False] * 4
    queue = [start]
    visited[start] = True

    while queue:
        city = queue.pop(0)
        print(cities[city], end=" ")

        for i in range(4):
            if graph[city][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)

def dfs(city, visited):
    visited[city] = True
    print(cities[city], end=" ")

    for i in range(4):
        if graph[city][i] == 1 and not visited[i]:
            dfs(i, visited)

print("BFS:")
bfs(0)

print("\nDFS:")
visited = [False] * 4
dfs(0, visited)