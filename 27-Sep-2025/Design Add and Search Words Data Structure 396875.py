# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_end = True
    def search(self, word: str) -> bool:
        def dfs(node, i):
            if not node:
                return False
            if i == len(word):
                return node.is_end
            ch = word[i]
            if ch == ".":
                for child in node.children:
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                idx = ord(ch) - ord('a')
                return dfs(node.children[idx], i + 1)

        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)