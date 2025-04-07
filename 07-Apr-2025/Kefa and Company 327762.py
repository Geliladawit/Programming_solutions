# Problem: Kefa and Company - https://codeforces.com/problemset/problem/580/B

arr = list(map(int, input().split()))
n = arr[0]
d = arr[1]
arr2 = []
for i in range(n):
    arr1 = list(map(int, input().split()))
    arr2.append(arr1)
arr2.sort(key=lambda x: x[0])
left = 0
max_friendship = 0
friendship_factor = 0
for i in range(n):
    friendship_factor += arr2[i][1]
    while arr2[i][0] - arr2[left][0] >= d:
        friendship_factor -= arr2[left][1]
        left += 1
    max_friendship = max(max_friendship, friendship_factor)
for _, friendship in arr2:
    max_friendship = max(max_friendship, friendship)

print(max_friendship)