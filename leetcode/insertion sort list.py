# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def insertionSortList(self, head):
        newnode=ListNode(0)
        newnode.next =head
        current=head
        pre=newnode
        while current:
            if current.next and  current.val<current.next.val:
                current=current.next
            pop=current.next
            current.next=current.next.next
            temp=newnode
            while pop.val>temp.next.val:
                temp=temp.next
            pop.next=temp.next
            temp.next=pop
        return newnode.next