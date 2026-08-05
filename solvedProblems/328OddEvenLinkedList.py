from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        if not head.next:
            return head

        oddNode = head
        evenNode = head.next
        evenNodeHead = evenNode

        while oddNode and evenNode:
            if evenNode.next:
                oddNode.next = evenNode.next
                oddNode = oddNode.next
            else:
                oddNode.next = evenNodeHead
                break
            if oddNode:
                evenNode.next = oddNode.next
                evenNode = evenNode.next
                oddNode.next = evenNodeHead

        return head

head = None
#node1 = ListNode(2)
#head.next = node1
#node1.next = head

print(Solution.hasCycle(Solution, head))
        