from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if (not headA) or (not headB):
            return None

        nodeDict = {}
        currNode = headA
        nodeDict[currNode] = currNode

        while currNode:
            currNode = currNode.next
            nodeDict[currNode] = currNode

        currNode = headB

        while currNode:
            if currNode in  nodeDict:
                return currNode     
            currNode = currNode.next
            
        return None

head = None
#node1 = ListNode(2)
#head.next = node1
#node1.next = head

print(Solution.hasCycle(Solution, head))
        