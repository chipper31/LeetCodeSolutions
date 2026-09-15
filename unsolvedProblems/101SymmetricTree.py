# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:

        if not root:
            return []

        leftTreeList = []
        rightTreeList = []

        self.leftHelper(self, root.left, leftTreeList)
        self.rightHelper(self, root.right, rightTreeList)
        #print(leftTreeList)
        #print(rightTreeList)

        return leftTreeList == rightTreeList

    def leftHelper(self, root, treeList):

        treeList.append(root.val)

        if root.left:
            self.leftHelper(self, root.left, treeList)
        else: 
            treeList.append(None)
        if root.right:
            self.leftHelper(self, root.right, treeList)
        else: 
            treeList.append(None)

    def rightHelper(self, root, treeList):

        treeList.append(root.val)

        if root.right:
            self.rightHelper(self, root.right, treeList)
        else: 
            treeList.append(None)

        if root.left:
            self.rightHelper(self, root.left, treeList)
        else: 
            treeList.append(None)

root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(2)

root.left = node2
root.right = node3

print(Solution.isSymmetric(Solution, root))