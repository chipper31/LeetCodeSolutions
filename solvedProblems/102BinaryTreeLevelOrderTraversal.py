#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:

        if not root:
            return []

        queue = []
        outList = []
        levelList = []
        currNode = root
        queue.append(root)
        levelLen = 1
        nodeLevelCount = 0

        while len(queue) > 0:
            currNode = queue[0]
            levelList.append(currNode.val)
            nodeLevelCount += 1

            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)

            queue.pop(0)
            if nodeLevelCount == levelLen:
                outList.append(levelList)
                levelList = []
                nodeLevelCount = 0
                levelLen = len(queue)

        return outList

root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

root.right = node2
node2.left = node3

print(Solution.levelOrder(Solution, root))