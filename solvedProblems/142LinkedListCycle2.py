from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        nodeDict = {}
        currNode = head
        nodeDict[currNode] = currNode

        while currNode:
            currNode = currNode.next
            if currNode in  nodeDict:
                return currNode
            nodeDict[currNode] = currNode    

        return None

head = None
#node1 = ListNode(2)
#head.next = node1
#node1.next = head

print(Solution.hasCycle(Solution, head))
        