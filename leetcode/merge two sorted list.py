# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        last=ListNode(20)
        tail=last
        # if list1==[] and list2==[]:
        #     return []
        while list1 and list2:
            if list1.val < list2.val:
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next
        if not list1:
            tail.nxet=list2
            list2=list2.next
        else:
            tail.next=list1
            list1=list1.next
        # while list1:
        #     tail.next=list1
        #     list1=list1.next
        # while list2:
        #     tail.next=list2
        #     list2=list2.next
        return tail.next
            