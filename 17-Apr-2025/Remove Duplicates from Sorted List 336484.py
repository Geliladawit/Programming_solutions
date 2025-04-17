# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        if curr:
            nextNode = curr.next
        while curr and nextNode:
            if curr.val == nextNode.val:
                curr.next = nextNode.next
                nextNode = curr.next
            else:
                curr = nextNode
                nextNode = nextNode.next
        return head