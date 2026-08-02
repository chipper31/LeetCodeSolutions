from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        middle = head
        newNode = head.next
        count = 2

        while newNode:
            if count == 2:
                count = 0
                middle = middle.next
            newNode = newNode.next
            count +=1

        return middle

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

print(Solution.middleNode(Solution, node1))