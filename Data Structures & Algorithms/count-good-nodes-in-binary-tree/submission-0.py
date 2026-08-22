# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodes=0
        def dfs(root,currentMax):
            if not root:
                return 
            if root.val>=currentMax:
                self.goodNodes+=1
            currentMax=max(currentMax,root.val)
            dfs(root.left,currentMax)
            dfs(root.right,currentMax)
        dfs(root,root.val)
        return self.goodNodes



