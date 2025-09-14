# Problem: A - Zhan's Blender - https://codeforces.com/gym/633600/problem/A

import math
t = int(input())
for _ in range(t):
    n = int(input())
    x,y = map(int, input().split())
    m = min(x,y)
    print(math.ceil(n/m))