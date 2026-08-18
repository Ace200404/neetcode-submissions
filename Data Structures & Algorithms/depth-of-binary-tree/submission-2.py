# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        stack=[[root,1]]
        num_max=0
        while stack:
            node,num=stack.pop()

            num_max=max(num,num_max)

            if node.left:
                stack.append([node.left,num+1])
            if node.right:
                stack.append([node.right,num+1])
        return num_max
