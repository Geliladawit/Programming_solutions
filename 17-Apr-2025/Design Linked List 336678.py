# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if self.length <= index:
            return -1
        currNode = self.head
        for _ in range(index):  
            currNode = currNode.next
        return currNode.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.length += 1        
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.length += 1
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        currNode = self.head
        while currNode.next:
            currNode = currNode.next
        currNode.next = new_node

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if self.length < index:
            return
        self.length += 1
        new_Node = Node(val) 
        if index == 0:
            new_Node.next = self.head
            self.head = new_Node
            return
        currNode = self.head
        while currNode and index > 1:
            currNode = currNode.next
            index -= 1
        new_Node.next = currNode.next
        currNode.next = new_Node

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if self.length <= index:
            return
        self.length -= 1
        if index == 0:
            self.head = self.head.next
            return
        currNode = self.head
        while currNode.next and index > 1:  
            currNode = currNode.next
            index -= 1
        currNode.next = currNode.next.next

    def listout(self):
        arr = []
        curr = self.head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        print(arr)
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)