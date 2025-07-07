# Problem: E - Zombie Invasion! - https://codeforces.com/gym/588094/problem/E

from collections import defaultdict

for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    damage = list(map(int, input().split()))
    position = list(map(int, input().split()))

    newDamage = defaultdict(int)
    for i in range(n):
        newDamage[abs(position[i])] += damage[i]

    # process closest zombie first
    position = sorted(newDamage.keys())

    isDead = False
    prevPosition, carry = 0, 0

    for i in range(len(position)):
        total = (k * (position[i] - prevPosition)) + carry
        if total < newDamage[position[i]]:
            isDead = True
            break

        carry = total - newDamage[position[i]]
        prevPosition = position[i]

    if isDead:
        print("NO")
    else:
        print("YES")