# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        ans = []

        for i in range(len(equations)):
            a, b = equations[i]
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))

        def dfs(start, dest, res, visited):
            if start == dest:
                return res

            if start in visited:
                return -1

            visited.add(start)
            for nei, val in graph[start]:
                temp = dfs(nei, dest, res * val, visited)
                if temp != -1:
                    return temp
                
            return -1

        for x, y in queries:
            if x not in graph or y not in graph:
                ans.append(-1)
            else:
                ans.append(dfs(x, y, 1.0, set()))

        return ans