class TrieNode:
    def __init__(self):
        self.children={}
        self.isWord=False
    def addWord(self,word):
        current=self
        for c in word:
            if c not in current.children:
                current.children[c]=TrieNode()
            current=current.children[c]
        current.isWord=True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for w in words:
            root.addWord(w)
        ROWS,COLUMNS=len(board),len(board[0])

        result, visited=set(),set()

        def dfs(r,c,node,word):
            if (r<0 or c<0 or r==ROWS or
                c==COLUMNS or (r,c) in visited
                or board[r][c] not in node.children):
                return
            visited.add((r,c))
            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.isWord:
                result.add(word)
            dfs(r-1,c,node,word)
            dfs(r,c-1,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c+1,node,word)
            visited.remove((r,c))

        for r in range(ROWS):
            for c in range(COLUMNS):
                dfs(r,c,root,'')

        return list(result)
            