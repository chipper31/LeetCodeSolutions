from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        currNode = head
        nums = []

        while currNode:
            nums.append(currNode.val)
            currNode = currNode.next

        for i in range(0, len(nums) >> 2):
            if nums[i] != nums[-i - 1]:
                return False
            
        return True

head = None
#node1 = ListNode(2)
#head.next = node1
#node1.next = head

print(Solution.hasCycle(Solution, head))
        