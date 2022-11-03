# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def insertionSortList(self, head):
        newnode=ListNode(0,head)
        newnode.next =head
        prev,current=head,head.next
        while current:
            if current.val>=prev.val:
                prev,current=current,current.next
                continue
            temp=newnode
            while current.val >temp.next.val:
                temp=temp.next
            prev.next=current.next
            current.next=temp.next
            temp.next=current 
            current=prev.next
        return newnode.next
   