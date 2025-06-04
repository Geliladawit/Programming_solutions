# Problem: F - Malak’s Stack - https://codeforces.com/gym/605795/problem/F

m = int(input())
N = 1
while N < m:
    N *= 2

max_balances = [0] * (2 * N)
total_balances = [0] * (2 * N)
values = [0] * m

for _ in range(m):
    parts = input().split()
    p = int(parts[0])
    t = int(parts[1])

    if t == 0:
        max_balances[N + p - 1] = 0
        total_balances[N + p - 1] = -1
    else:
        x = int(parts[2])
        values[p - 1] = x
        max_balances[N + p - 1] = 1
        total_balances[N + p - 1] = 1

    j = (N + p - 1) // 2
    while j >= 1:
        total_balances[j] = total_balances[2 * j] + total_balances[2 * j + 1]
        max_balances[j] = max(
            max_balances[2 * j + 1],
            max_balances[2 * j] + total_balances[2 * j + 1],
            0
        )
        j //= 2

    if max_balances[1] == 0:
        print(-1)
        continue

    j = 1
    offset = 0
    while j < N:
        if max_balances[2 * j + 1] + offset > 0:
            j = 2 * j + 1
        else:
            offset += total_balances[2 * j + 1]
            j = 2 * j

    print(values[j - N])