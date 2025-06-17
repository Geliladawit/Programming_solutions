# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        
        visited = set()
        def dfs(node):
            if node == destination:
                return True
            
            visited.add(node)

            for i in adj[node]:
                if not i in visited:
                    found = dfs(i)
                    if found:
                        return True
            return False
        return dfs(source)