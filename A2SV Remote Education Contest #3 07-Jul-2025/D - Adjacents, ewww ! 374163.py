# Problem: D - Adjacents, ewww ! - https://codeforces.com/gym/588094/problem/D

def solve():
      n = int(input())
      if n==2:
         return [[-1]]
      if n==1:
         return [[1]]
      indexes =  [[(i + j) % 2, i, j] for i in range(n) for j in range(n)]
      indexes.sort()
      final_matrix = [[0 for i in range(n)] for j in range(n)]
      curr = 1
      #in this case color means either 1 or 0
       for color, i, j in indexes:
           final_matrix[i][j] = curr
           curr += 1
       return final_matrix
tests = int(input())
for test in range(tests):
      answer = solve()
      for row in answer:
          print(*row)