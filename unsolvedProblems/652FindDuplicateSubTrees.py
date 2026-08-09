from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> list[Optional[TreeNode]]:

        outList = self.helper(self, root, [])

        return outList

    def helper(self, root, outList):

        for i in range(0,len(outList)):
            outList[i].append(root.val)
        #print(outList)
        outList.append([root.val])

        if root.left:
            (self.helper(self, root.left, outList))

        if root.right:
            (self.helper(self, root.right, outList))

        return outList

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node1.left = node2
node1.right = node3
node2.left = node4

print(Solution.findDuplicateSubtrees(Solution, node1))