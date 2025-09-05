# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

n,k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = -1
if k == 0:
    res = arr[0] - 1 if arr[0] > 1 else -1
elif k == n:
    res = arr[-1] 
elif arr[k-1] != arr[k]:
    res = arr[k - 1]
print(res)
