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

        point=head

        while point:
            deepCopy[point]=Node(point.val)
            point=point.next
        
        point=head
        while point:
            copy=deepCopy[point]
            copy.next=deepCopy[point.next]
            copy.random=deepCopy[point.random]
            point=point.next
        
        return deepCopy[head]
            