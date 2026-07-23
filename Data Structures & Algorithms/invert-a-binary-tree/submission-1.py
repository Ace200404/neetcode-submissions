# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # check if the root is there
        if not root:
            return None

        # make a data set to access and add roots
        q=deque([root])

        while q:
            node=q.popleft()
            node.left, node.right= node.right, node.left

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        # add roots to the data set if there is any
        return root
        