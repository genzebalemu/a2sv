class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):  
        newnode = ListNode(0)
        newnode.next = head
        current,pre = head, newnode
        while current :
            while current.next and current.val == current.next.val:
                current = current.next 
            if pre.next == current:
                current = current.next
                pre = pre.next
            else:
                pre.next=current.next
                current=pre.next
        return newnode.next
    