# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head == None or head.next == None:
            return


        count=0
        temp=head
        while temp!=None:
            count=count+1
            temp=temp.next

        if count == n:
            head=head.next
            return head    

        c=1
        temp=head
        while c < (count-n):
            temp=temp.next
            c=c+1
        temp.next=temp.next.next
        return head    


        