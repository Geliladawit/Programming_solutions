# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076

n, m = map(int, input().split())
degree_count = [0] * (n + 1) 
for _ in range(m):
    u, v = map(int, input().split())
    degree_count[u] += 1
    degree_count[v] += 1

if len(set(degree_count[1:])) == 1:
    print("YES")
else:
    print("NO")
