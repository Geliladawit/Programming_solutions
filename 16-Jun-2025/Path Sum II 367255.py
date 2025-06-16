# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        result = []
        def dsf(node, path, running_sum):
            running_sum += node.val
            p = path+[node.val]

            if not node.left and not node.right and running_sum == targetSum:
                result.append(p)
            if node.left:
                dsf(node.left, p,running_sum)
            if node.right:
                dsf(node.right, p,running_sum)

        dsf(root, [], 0)
        return result