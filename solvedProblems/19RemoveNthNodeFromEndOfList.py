from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head.next:
            return None

        nodeA = head
        nodeB = head

        for i in range(0,n):
            nodeA = nodeA.next

        if not nodeA:
            return nodeB.next

        while nodeA:
            nodeA = nodeA.next
            nodeB = nodeB.next

        nodeB.next = nodeB.next.next

        return head

head = None
#node1 = ListNode(2)
#head.next = node1
#node1.next = head

print(Solution.hasCycle(Solution, head))
        