# Problem: Maximum Binary Tree - https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mx = max(nums)
        idx = nums.index(mx)
        tree = TreeNode(mx) 
        tree.left = self.constructMaximumBinaryTree(nums[:idx])
        tree.right = self.constructMaximumBinaryTree(nums[idx+1:])
        return tree