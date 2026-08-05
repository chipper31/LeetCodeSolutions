from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False

        slowNode = head
        fastNode = head.next

        while fastNode:
            if slowNode ==  fastNode:
                return True
            fastNode = fastNode.next
            slowNode = slowNode.next
            if not fastNode:
                return False
            fastNode = fastNode.next      

        return False

head = None
#node1 = ListNode(2)
#head.next = node1
#node1.next = head

print(Solution.hasCycle(Solution, head))
        