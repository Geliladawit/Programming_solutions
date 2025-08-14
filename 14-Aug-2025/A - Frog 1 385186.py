# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

n = int(input())
rocks = list(map(int, input().split()))
dp = [0]*n
dp[1] = abs(rocks[1] - rocks[0])
for i in range(2,n):
  dp[i] = min(dp[i-1] + abs(rocks[i] - rocks[i-1]), dp[i-2] + abs(rocks[i] - rocks[i-2]))
  
print(dp[-1])