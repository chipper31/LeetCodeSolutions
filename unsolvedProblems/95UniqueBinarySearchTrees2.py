from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        
        nums = []
        roots = []
        for i in range(0,n):
            nums.append(i+1)

        node1 = TreeNode(1)
        nums.pop(0)
        roots.append(self.helper(self, node1, nums))

        return None

    def helper(self, root, nums):

        if not nums:
            return root

        while nums:
            newNode = TreeNode(nums.pop(0))
            if newNode.val > root.val:
                root.right = self.helper(self, newNode, nums)
            if newNode.val < root.val:
                root.left = self.helper(self, newNode, nums)

Solution.generateTrees(Solution, 3)

