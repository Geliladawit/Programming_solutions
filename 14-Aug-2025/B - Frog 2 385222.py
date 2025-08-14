# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

n,k = map(int, input().split())
rocks = list(map(int, input().split()))
dp = [float('inf')] * n
dp[0] = 0
dp[1] = abs(rocks[1] - rocks[0])
for i in range(2, n):
    for j in range(1, min(k, i) + 1):
        dp[i] = min(dp[i], dp[i - j] + abs(rocks[i] - rocks[i - j]))

print(dp[-1])
