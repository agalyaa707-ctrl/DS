courses = ["Python", "AI", "Cloud", "Cyber Security"]
cost = [2000, 3000, 2500, 3500]
benefit = [60, 90, 70, 100]

capacity = 5
n = len(courses)

dp = [[0] * (capacity + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for w in range(capacity + 1):
        if cost[i - 1] <= w * 1000:
            dp[i][w] = max(
                dp[i - 1][w],
                benefit[i - 1] + dp[i - 1][w - cost[i - 1] // 1000]
            )
        else:
            dp[i][w] = dp[i - 1][w]

print("Maximum Training Benefit:", dp[n][capacity])