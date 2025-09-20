# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        less = ListNode(0)
        great = ListNode(0)
        less_tail = less
        great_tail = great
        while curr:
            if curr.val >= x:
                great_tail.next = curr
                great_tail = great_tail.next
            else:
                less_tail.next = curr
                less_tail = less_tail.next
            curr = curr.next
        great_tail.next = None   
        less_tail.next = great.next
        return less.next