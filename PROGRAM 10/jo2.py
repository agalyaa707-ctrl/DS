cost = [
    [8, 6, 9],
    [7, 5, 6],
    [4, 8, 7]
]

n = 3
best = 999
solution = []

def allocate(i, selected, total, result):
    global best, solution

    if i == n:
        if total < best:
            best = total
            solution = result[:]
        return

    if total >= best:
        return

    for j in range(n):
        if j not in selected:
            result.append(j)
            allocate(i + 1, selected + [j],
                     total + cost[i][j], result)
            result.pop()

allocate(0, [], 0, [])

for i in range(n):
    print("Staff", i + 1, "-> Room", solution[i] + 1)

print("Minimum Cost:", best)