"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        deepCopy={None:None}

        current=head

        while current:
            deepCopy[current]=Node(current.val)
            current=current.next
        
        current=head
        while current:
            copy=deepCopy[current]
            copy.next=deepCopy[current.next]
            copy.random=deepCopy[current.random]
            current=current.next
        return deepCopy[head]