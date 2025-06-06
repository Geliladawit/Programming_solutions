# Problem: F - Love Birds - https://codeforces.com/gym/613405/problem/F

import bisect

def solve():
    inputCount = int(input())
    while inputCount:
        ip = input()
        if not ip: continue
        n, m = map(int, ip.split())

        flowers, a = [], []
        for _ in range(m):
            x, y = map(int, input().split())
            flowers.append((x, y))
            a.append(x)
        
        a_sorted = sorted(a)
        pre = [0] * (m + 1)
        for i in range(m - 1, -1, -1):
            pre[i] = pre[i + 1] + a_sorted[i]
        
        ans = 0
        
        for i in range(m):
            x, y = flowers[i]
            pos = bisect.bisect_right(a_sorted, y)
            count = m - pos
            sum_ = pre[pos] if pos < m else 0
            
            if x <= y:
                sum_ += x
                count += 1
            
            if count >= n:
                current = pre[m - n] if (m - n) >= 0 else 0
            else:
                current = sum_ + (n - count) * y
            
            if current > ans:
                ans = current
        
        print(ans)
        inputCount -= 1

solve()