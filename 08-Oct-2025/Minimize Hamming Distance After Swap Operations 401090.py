# Problem: Minimize Hamming Distance After Swap Operations - https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/description/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            self.parent[pb] = pa

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:    
        n = len(source)
        uf = UnionFind(n)
        for a, b in allowedSwaps:
            uf.union(a, b)

        groups = defaultdict(list)
        for i in range(n):
            groups[uf.find(i)].append(i)
        
        res = 0
        for comp in groups.values():
            src_vals = Counter(source[i] for i in comp)
            tgt_vals = Counter(target[i] for i in comp)
            matches = sum((src_vals & tgt_vals).values())
            res += len(comp) - matches
        return res