# Problem: E - Sound Compression - https://codeforces.com/gym/613405/problem/E

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

carr = []
i = 0
while i < n:
    count = 1
    j = i + 1
    while j < n and arr[j] == arr[i]:
        count += 1
        j += 1
    carr.append((arr[i], count))
    i = j

limit = min(pow(2, 8 * m // n), pow(2, 20))
ans = 0
l = 0
curr = 0

for r in range(len(carr)):
    curr += carr[r][1]
    while r - l + 1 > limit:
        curr -= carr[l][1]
        l += 1
    ans = max(ans, curr)

print(n - ans)