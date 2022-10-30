# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        curr=slow.next
        prev=slow.next=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        first,curr=head,prev
        while curr:
            temp1,temp2=first.next,curr.next
            first.next=curr
            curr.next=temp1
            first,curr=temp1,temp2
            