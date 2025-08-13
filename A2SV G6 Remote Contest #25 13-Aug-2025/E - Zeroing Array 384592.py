# Problem: E - Zeroing Array - https://codeforces.com/gym/628023/problem/E

n = int(input())
a = list(map(int, input().split()))

t = sum(a)
max_v = max(a)

if t % 2 == 0 and max_v <= t - max_v:
    print("YES")
else:
    print("NO")