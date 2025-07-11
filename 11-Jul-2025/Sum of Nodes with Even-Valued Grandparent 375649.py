# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        running_sum = 0
        def dfs(node, parent = None, grandp = None):
            nonlocal running_sum
            if not node:
                return
            if grandp and grandp.val % 2 == 0:
                running_sum += node.val
            
            dfs(node.left, node, parent)
            dfs(node.right, node, parent)

        dfs(root)
        return running_sum            