from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        size = 0

        if not head:
            return None

        currNode = head

        while currNode:
            size += 1
            currNode = currNode.next

        offSet = k % size

        fastNode = head
        slowNode = head

        for i in range(0, offSet):
            fastNode = fastNode.next

        while fastNode.next:
            fastNode = fastNode.next
            slowNode = slowNode.next

        fastNode.next = head
        head = slowNode.next
        slowNode.next = None

        return head

