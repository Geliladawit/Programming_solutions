# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        email_to_name = {}
        for acc in accounts:
            name = acc[0]
            first_email = acc[1]
            for email in acc[1:]:
                graph[first_email].append(email)
                graph[email].append(first_email)
                email_to_name[email] = name
        visited = set()
        res = []
        def dfs(email, component):
            visited.add(email)
            component.append(email)
            for nei in graph[email]:
                if nei not in visited:
                    dfs(nei, component)
        for email in email_to_name:
            if email not in visited:
                component = []
                dfs(email, component)
                res.append([email_to_name[email]] + sorted(component))
        return res