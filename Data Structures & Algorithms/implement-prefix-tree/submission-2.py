class TreeNode:
    def __init__(self):
        self.children={}
        self.word=False
class PrefixTree:

    def __init__(self):
        self.root=TreeNode()

    def insert(self, word: str) -> None:
        current=self.root

        for i in word:
            if i not in current.children:
                current.children[i]=TreeNode()
            current=current.children[i]
        current.word=True


    def search(self, word: str) -> bool:
        current=self.root

        for i in word:
            if i not in current.children:
                return False
            current=current.children[i]
        return current.word

    def startsWith(self, prefix: str) -> bool:

        current=self.root

        for i in prefix:
            if i not in current.children:
                return False
            current=current.children[i]
        return True
        
        