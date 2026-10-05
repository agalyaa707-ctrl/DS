cost = [
    [12, 7, 9, 8],
    [6, 5, 8, 7],
    [9, 8, 6, 5],
    [7, 9, 5, 6]
]

n = 4
best = 999
answer = []

def solve(i, used, total, result):
    global best, answer

    if i == n:
        if total < best:
            best = total
            answer = result[:]
        return

    if total >= best:
        return

    for j in range(n):
        if j not in used:
            result.append(j)
            solve(i + 1, used | {j},
                  total + cost[i][j], result)
            result.pop()

solve(0, set(), 0, [])

for i in range(n):
    print("Developer", i + 1, "-> Module", answer[i] + 1)

print("Minimum Cost:", best)