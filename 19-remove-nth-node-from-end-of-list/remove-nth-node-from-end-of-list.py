# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length=0
        temp=head
        while temp!=None:
            length=length+1
            temp=temp.next

        if length == n:
            return head.next   

        pos=1
        temp=head
        while pos < (length-n):
            temp=temp.next
            pos=pos+1
        temp.next=temp.next.next
        return head    


        