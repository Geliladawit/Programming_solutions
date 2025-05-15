# Problem: Merge Two Binary Trees - https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(root_1, root_2):
            if not root_1 and not root_2:
                return None
            elif not root_1 and root_2:
                return root_2
            elif root_1 and not root_2:
                return root_1
            else:
                root = TreeNode(root_1.val + root_2.val)
                root.left = merge(root_1.left, root_2.left)
                root.right = merge(root_1.right, root_2.right)
                return root
        return merge(root1, root2)
           
            

