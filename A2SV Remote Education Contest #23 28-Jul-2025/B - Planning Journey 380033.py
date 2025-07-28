# Problem: B - Planning Journey - https://codeforces.com/gym/625306/problem/B

def max_journeys(n, k, weather):
    journeys = 0
    i = 0
    while i <= n - k:
        if weather[i] == 1:
            i += 1
            continue
        valid = True
        for j in range(i, i + k):
            if weather[j] == 1:
                valid = False
                i = j + 1
                break
        if valid:
            journeys += 1
            i += k + 1
    return journeys

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    weather = list(map(int, input().split()))
    print(max_journeys(n, k, weather))
