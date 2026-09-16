# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:

        if len(inorder) == 1:
            root = TreeNode(inorder[0])
            return root

        if len(inorder) <= 0:
            return None

        root = TreeNode(postorder[-1])
        postorder.pop(-1)

        for i in range(0,len(inorder)):
            if inorder[i] == root.val:
                sizeRightTree = len(inorder[i+1:])
                if sizeRightTree == 0:
                    root.left = self.buildTree(self, inorder[0:i], postorder)
                    root.right = self.buildTree(self, inorder[i+1:], [])
                else:
                    root.left = self.buildTree(self, inorder[0:i], postorder[0:-sizeRightTree])
                    root.right = self.buildTree(self, inorder[i+1:], postorder[-sizeRightTree:])
                break

        return root