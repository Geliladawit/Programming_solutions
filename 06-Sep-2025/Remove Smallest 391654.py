# Problem: Remove Smallest - https://codeforces.com/problemset/problem/1399/A

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    if n == 1:
        print("YES")
        continue

    i = 0
    while i < len(arr) - 1:
        if abs(arr[i] - arr[i + 1]) <= 1:
            arr.pop(i)
        else:
            i += 1
    if len(arr) == 1:
        print("YES")
    else:
        print("NO")