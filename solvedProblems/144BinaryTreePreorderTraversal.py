from typing import Optional
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:

        treeList = []

        self.helper(self, root, treeList)

        return treeList

    def helper(self, root, treeList):

        treeList.append(root.val)

        if root.left:
            self.helper(self, root.left, treeList)

        if root.right:
            self.helper(self, root.right, treeList)

root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

root.right = node2
node2.left = node3

print(Solution.preorderTraversal(Solution, root))