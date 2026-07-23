class MinStack:

    def __init__(self):
        self.stack=[]
        self.lowest=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        val=min(val,self.lowest[-1] if self.lowest else val)
        self.lowest.append(val)

    def pop(self) -> None:
        
        self.stack.pop()
        self.lowest.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.lowest[-1]
