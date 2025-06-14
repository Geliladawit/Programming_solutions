# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

def adj_list_to_matrix(n, e):
    m = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for t in e[i]:
            m[i][t - 1] = 1
    
    return m
n = int(input())
e = []
for _ in range(n):
    d = list(map(int, input().split()))
    o_count = d[0]
    o_edges = d[1:o_count + 1]
    e.append(o_edges)

adj_matrix = adj_list_to_matrix(n, e)
for r in adj_matrix:
    print(' '.join(map(str, r)))
