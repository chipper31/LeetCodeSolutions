from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        nodeDict = {}

        OgCurrNode = head
        headCopy = Node(head.val)
        CpCurrNode = headCopy

        while OgCurrNode:
            nodeDict[OgCurrNode] = CpCurrNode
            if OgCurrNode.next:
                CpCurrNode.next = Node(OgCurrNode.next.val)
            OgCurrNode = OgCurrNode.next
            CpCurrNode = CpCurrNode.next

        OgCurrNode = head
        CpCurrNode = headCopy

        while OgCurrNode:
            if OgCurrNode.random in nodeDict:
                CpCurrNode.random = nodeDict[OgCurrNode.random]
            OgCurrNode = OgCurrNode.next
            CpCurrNode = CpCurrNode.next
        
        return headCopy