cost = [
    [9, 2, 7],
    [6, 4, 3],
    [5, 8, 1]
]

best_cost = 999
best = []

def assign(developer, projects, cost_so_far, result):
    global best_cost, best

    if developer == 3:
        if cost_so_far < best_cost:
            best_cost = cost_so_far
            best = result[:]
        return

    if cost_so_far >= best_cost:
        return

    for project in range(3):
        if project not in projects:
            result.append(project)
            assign(developer + 1,
                   projects + [project],
                   cost_so_far + cost[developer][project],
                   result)
            result.pop()

assign(0, [], 0, [])

for i in range(3):
    print("Developer", i + 1, "-> Project", best[i] + 1)

print("Minimum Cost:", best_cost)