"""
The problem can be transfered to Knapsack problem:

1. there are n-1 steps (not n, because we need at least 2 steps)
2. j bricks is needed to build the j-th steps.
3. for each step, we decide whether to build or not to build it

dp[i][j] = the combination of using i bricks to build 1~j steps
dp[i][j] = dp[i][j-1] (not build) + dp[i-j][j-1] (build)
"""


def answer(n):
    dp = [[0] * n for _ in range(n + 1)]
    dp[0][0] = dp[1][1] = dp[2][2] = 1

    for j in range(1, n):
        for i in range(n + 1):
            dp[i][j] = dp[i][j - 1]
            if i >= j:
                dp[i][j] += dp[i - j][j - 1]

    return dp[-1][-1]

for i in range(3, 201):
    print(i, answer(i))
