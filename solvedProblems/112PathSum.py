# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:

        if not root:
            return False

        pathBool = []

        self.helper(self, root, targetSum, 0, pathBool)

        if pathBool:
            return True

        return False

    def helper(self, root, targetSum, sum, pathBool):

        sum += root.val

        if root.left:
            self.helper(self, root.left, targetSum, sum, pathBool)

        if root.right:
            self.helper(self, root.right, targetSum, sum, pathBool)

        if (not root.left) and (not root.right):
            if sum == targetSum:
                print("found sum!")
                pathBool.append(sum)

        return

root = TreeNode(-2)
node2 = TreeNode(0)
node3 = TreeNode(-3)

root.left = node2
root.right = node3

print(Solution.hasPathSum(Solution, root, -5))