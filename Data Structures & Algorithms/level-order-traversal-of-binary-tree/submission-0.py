# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque([root])
        result=[]
        while root and q:
            level_count=len(q)
            node_list=[]
            while level_count>0:
                node=q.popleft()
                node_list.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level_count-=1
            result.append(node_list)
        return result
                

