class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        fast=head
        slow=head
        # find middle elment
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        #  reverse second halve 
        pre=None
        while slow:
            temp=slow.next
            slow.next=pre
            pre=slow
            slow=temp
        left,right=head,pre
        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True