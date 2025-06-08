# Problem: E - Skibidus and Sigma - https://codeforces.com/gym/603156/problem/E

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    total_score = 0
    totals = []  
    for i in range(n):
        arr = list(map(int, input().split()))
        prefix_sum = 0
        score_arr = 0
        for x in arr:
            prefix_sum += x
            score_arr += prefix_sum
        total_score += score_arr
        totals.append(prefix_sum)  

    totals.sort(reverse=True)
    extra = 0
    for i, tot in enumerate(totals):
        extra += (n - 1 - i) * tot  
    extra *= m

    answer = total_score + extra
    print(answer)