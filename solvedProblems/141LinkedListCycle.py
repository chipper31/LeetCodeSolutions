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

        nodeDict = {
            head: head.val
        }
        newNode = head.next

        while newNode:
            if newNode in  nodeDict:
                return True
            nodeDict[newNode] = newNode.val
            newNode = newNode.next

        return False

head = None
#node1 = ListNode(2)
#head.next = node1
#node1.next = head

print(Solution.hasCycle(Solution, head))
        