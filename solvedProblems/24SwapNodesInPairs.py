from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head:
            if head.next:
                tempNode = ListNode(0,head.next)
                head.next = self.swapPairs(self, head.next.next)
                tempNode.next.next = head
                return tempNode.next
            return head
        return None

node4 = ListNode(4, None)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

Solution.swapPairs(Solution, node1)