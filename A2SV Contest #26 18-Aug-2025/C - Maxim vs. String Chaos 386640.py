# Problem: C - Maxim vs. String Chaos - https://codeforces.com/gym/629689/problem/C

t = int(input())
answer = []
for _ in range(t):
    n, q = map(int, input().split())
    a = input().strip()
    b = input().strip()


    prefA = [[0]*26 for _ in range(n+1)]
    prefB = [[0]*26 for _ in range(n+1)]

    for i in range(n):
        for c in range(26):
            prefA[i+1][c] = prefA[i][c]
            prefB[i+1][c] = prefB[i][c]
        prefA[i+1][ord(a[i])-97] += 1
        prefB[i+1][ord(b[i])-97] += 1    

    for _ in range(q):
        l, r = map(int, input().split())

        freqA = [prefA[r][c] - prefA[l-1][c] for c in range(26)]
        freqB = [prefB[r][c] - prefB[l-1][c] for c in range(26)]
        
        ops = 0
        for c in range(26):
            if freqB[c] > freqA[c]:
                ops += freqB[c] - freqA[c]
        
        answer.append(ops)

for ans in answer:
    print(ans)