equipment = ["Monitor", "Scanner", "Ventilator", "X-Ray"]
weight = [2, 5, 3, 4]
value = [40, 80, 70, 90]

capacity = 7
n = len(equipment)

dp = [[0] * (capacity + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for w in range(capacity + 1):
        if weight[i - 1] <= w:
            dp[i][w] = max(
                dp[i - 1][w],
                value[i - 1] + dp[i - 1][w - weight[i - 1]]
            )
        else:
            dp[i][w] = dp[i - 1][w]

print("Maximum Equipment Value:", dp[n][capacity])