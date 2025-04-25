# Problem: Min Stack - https://leetcode.com/problems/min-stack/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class MinStack(object):

    def __init__(self):
        self.head = None
        self.st = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.st.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if not self.head:
            return
        self.head = self.head.next
        if self.st:
            self.st.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.head.val

    def getMin(self):
        """
        :rtype: int
        """
        if self.st:
            ans = min(self.st)
            return ans


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()