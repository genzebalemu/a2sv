class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None 
        while len(lists) > 1:
            mergedlists=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                if i+1 < len(lists):
                    l2 = lists[i+1]
                else:
                    l2=None    
                mergedlists.append(self.merge(l1,l2))
            lists = mergedlists    
        return lists[0]
    def merge(self,l1,l2):
        last=ListNode()
        tail=last
        while l1 and l2:
            if l2.val < l1.val:
                tail.next=l2
                l2= l2.next
            else:
                tail.next = l1
                l1=l1.next
            tail = tail.next
        if l1:
            tail.next=l1
            l1=l1.next
        if l2:
            tail.next=l2
            l2=l2.next
        return last.next
            