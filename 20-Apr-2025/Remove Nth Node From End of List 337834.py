# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1, head)
        fast= slow = dummy
        index = 0
        while fast and fast.next:
            fast = fast.next
            if index >= n:
                slow = slow.next
            index += 1
        slow.next = slow.next.next
        return dummy.next
