# Problem: C - Binary Deque - https://codeforces.com/gym/633600/problem/C

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    total = sum(arr)
    if total < s:
        print(-1)
        continue
    if total == s:
        print(0)
        continue

    l, runnin_sum, m = 0, 0, -1
    for r in range(n):
        runnin_sum += arr[r]
        while runnin_sum > s:
            runnin_sum -= arr[l]
            l += 1
        if runnin_sum == s:
            m = max(m, r - l + 1)

    print(n - m if m != -1 else -1)
