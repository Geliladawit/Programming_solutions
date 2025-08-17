# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

n = int(input())
dp = [0, 0, 0]
for _ in range(n):
    a, b, c = map(int, input().split())
    prev_a, prev_b, prev_c = dp[0], dp[1], dp[2]
    dp[0] = a + max(prev_b, prev_c)
    dp[1] = b + max(prev_a, prev_c)
    dp[2] = c + max(prev_a, prev_b)

print(max(dp))