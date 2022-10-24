class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head_ptr = temp_ptr = ListNode()
        while list1 or list2:
            if list1 and (not list2 or list1.val <= list2.val):
                temp_ptr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                temp_ptr.next = ListNode(list2.val)
                list2 = list2.next
            temp_ptr = temp_ptr.next
        return head_ptr.next
            