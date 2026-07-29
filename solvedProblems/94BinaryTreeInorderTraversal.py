from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        outList = []
        self.helper(self, root, outList)
        return outList
    
    def helper(self, root, outList):
        if root:
            self.helper(self, root.left, outList)
            outList.append(root.val)
            self.helper(self, root.right, outList)
    


root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

root.right = node2
node2.left = node3

print(Solution.inorderTraversal(Solution, root))
        