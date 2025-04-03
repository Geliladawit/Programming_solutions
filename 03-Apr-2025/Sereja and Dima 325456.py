# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

n = int(input())
cards = list(map(int, input().split()))
sereja= 0
dima = 0
left = 0
right = n - 1
c = True
while left <= right:
    if cards[left] > cards[right]:
        card = cards[left]
        left += 1
    else:
        card = cards[right]
        right -= 1

    if c:
        sereja += card
    else:
        dima += card
    c = not c
print(sereja, dima)
