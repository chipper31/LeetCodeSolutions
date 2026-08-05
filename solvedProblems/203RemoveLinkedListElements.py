from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if not head:
            return None

        while head:
            if head.val == val:
                head = head.next
            else:
                break

        currNode = head

        while currNode:
            if currNode.next:
                if currNode.next.val == val:
                    currNode.next = currNode.next.next
                    continue
            currNode = currNode.next

        return head

head = None
#node1 = ListNode(2)
#head.next = node1
#node1.next = head

print(Solution.hasCycle(Solution, head))
        