# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))

        min_path_score = float('inf')
        visited_cities = [False] * (n + 1)

        queue = deque()
        queue.append(1)
        visited_cities[1] = True

        while queue:
            current_city = queue.popleft()

            for neighbor_city, distance in graph[current_city]:
                min_path_score = min(min_path_score, distance)

                if not visited_cities[neighbor_city]:
                    visited_cities[neighbor_city] = True
                    queue.append(neighbor_city)
        
        return min_path_score