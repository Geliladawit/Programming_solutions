# Problem: E - NATOLI's String Quest - https://codeforces.com/gym/605795/problem/E

s = input()
n = len(s)
t = []
u = []
remain = [None] * n

remain[-1] = s[-1]
for i in range(n-2, -1, -1):
    remain[i] = min(s[i], remain[i+1])
 
i = 0
while i<n or t:
    if t and (i>=n or t[-1]<= remain[i]):
        u.append(t.pop())

    else:
        t.append(s[i])
        i += 1

print("".join(u))
