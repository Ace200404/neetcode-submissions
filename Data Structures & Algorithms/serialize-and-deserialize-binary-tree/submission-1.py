# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        lst=[]
        def dfs(root):
            if not root:
                lst.append('N')
                return 
            lst.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        return','.join(lst)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values=data.split(',')
        self.position=0
        def dfs():
            if values[self.position]=='N':
                self.position+=1
                return None

            node=TreeNode(int(values[self.position]))
            self.position+=1
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()
