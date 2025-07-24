# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        n = len(quiet)
        indegree = [0] * n
        ans = [i for i in range(n)]

        for rich, poor in richer:
            graph[rich].append(poor)
            indegree[poor] += 1

        queue = deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            curr = queue.popleft()

            for nei in graph[curr]:
                curr_quiet = ans[curr]
                nei_quiet = ans[nei]

                if quiet[curr_quiet] < quiet[nei_quiet]:
                    ans[nei] = curr_quiet

                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return ans