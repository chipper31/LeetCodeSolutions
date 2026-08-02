from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head:
            if head.next:
                newHead = self.reverseList(self, head.next)
            else:
                return head

            if head.next.next == None:
                head.next.next = head
                head.next = None
                return newHead
        return head

node5 = ListNode(5, None)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

Solution.reverseList(Solution, node1)