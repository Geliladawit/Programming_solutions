# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(root, data):
            if root is None:
                return TreeNode(data)
            if data < root.val:
                root.left = insert(root.left, data)
                return root
            if data > root.val:
                root.right = insert(root.right, data)
                return root

        return insert(root, val)
