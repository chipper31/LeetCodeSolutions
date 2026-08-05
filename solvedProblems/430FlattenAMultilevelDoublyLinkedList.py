from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        currNode = head

        while currNode:
            if currNode.child:
                childHead = self.flatten(currNode.child)
                childTail = self.getTail(currNode.child)
                currNode.child = None
                childHead.prev = currNode
                childTail.next = currNode.next
                if childTail.next:
                    childTail.next.prev = childTail
                currNode.next = childHead
            currNode = currNode.next

        return head

#returns the tail of the given head of linked list
    def getTail(self, head):

        currNode = head

        while currNode.next:
            currNode = currNode.next

        return currNode