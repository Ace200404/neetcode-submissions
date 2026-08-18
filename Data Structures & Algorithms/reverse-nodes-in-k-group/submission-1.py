# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=node=ListNode(0,head)

        while True:
            kth=self.merging(node,k)
            
            if not kth:
                break
            nextGroup=kth.next
            prev,curr = kth.next,node.next
            while curr!=nextGroup:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            
            temp=node.next
            node.next=kth
            node=temp
        return dummy.next



    
    def merging(self,current,k):
        while current and k>0:
            current=current.next
            k-=1
        return current