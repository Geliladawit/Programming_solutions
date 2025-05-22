# Problem: Print the Elements of a Linked List - https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem

def printLinkedList(head):
    node = head
    while node:
        print(node.data)
        node = node.next