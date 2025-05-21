# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            curr = node
            prev = None

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        l1 = reverse(l1)
        l2 = reverse(l2)
        carry = 0
        dummy = ListNode()
        curr = dummy

        while l1 or l2 or carry:
            total = 0
            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            total += carry
            carry = total // 10
            curr.next = ListNode((total % 10)) 
            curr = curr.next

        return reverse(dummy.next)