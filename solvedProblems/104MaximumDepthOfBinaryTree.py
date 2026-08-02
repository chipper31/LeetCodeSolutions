from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return self.helper(self, root, 1)

    def helper(self, root, depth):
        Ldepth = 0
        Rdepth = 0
        if (not root.left) and (not root.right):
            return depth

        if root.left:
            Ldepth = self.helper(self, root.left, depth+1)
        if root.right:
            Rdepth = self.helper(self, root.right, depth+1)
        return max(Ldepth, Rdepth)

node3 = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)
node3.left = node9
node3.right = node20
node20.left = node15
node20.right = node7

print(Solution.maxDepth(Solution, node3))