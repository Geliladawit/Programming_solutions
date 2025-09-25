# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.score = 0
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        diff = val - self.map.get(key, 0)
        self.map[key] = val
        current = self.root
        for ch in key:
            idx = ord(ch) - ord('a')
            if not current.children[idx]:
                current.children[idx] = TrieNode()
            current = current.children[idx]
            current.score += diff

    def sum(self, prefix: str) -> int:
        current = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not current.children[idx]:
                return 0
            current = current.children[idx]
        return current.score
    


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)