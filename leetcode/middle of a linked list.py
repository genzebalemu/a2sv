# Definition for singly-linked list.
class ListNode(object):
    def init(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def getLen(self, head):
        temp = head
        len = 0
        while (temp != None):
            len += 1
            temp = temp.next
            
        return len
    
    def middleNode(self, head):
        if head != None:
            len = self.getLen(head)
            temp = head
            midIdx = len // 2
            while midIdx != 0:
                temp = temp.next
                midIdx -= 1
            return temp
