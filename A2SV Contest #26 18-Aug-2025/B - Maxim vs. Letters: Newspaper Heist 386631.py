# Problem: B - Maxim vs. Letters: Newspaper Heist - https://codeforces.com/gym/629689/problem/B

from collections import Counter

h=input()
t=input()
f=Counter(h)
ch=Counter(t)
for i in ch:
    if i != " " and ch[i] >f[i]:
        print("NO")
        exit()
print("YES")
