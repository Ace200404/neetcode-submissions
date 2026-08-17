# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=startGroup=ListNode(0,head)
        
        while True:
            kth = self.kGroup(startGroup,k)
            if not kth:
                break
            nextGroup=kth.next

            prev,curr=kth.next,startGroup.next
            
            while curr!=nextGroup:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            
            temp=startGroup.next
            startGroup.next=kth
            startGroup=temp
        
        return dummy.next

    
    def kGroup(self,curr,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr