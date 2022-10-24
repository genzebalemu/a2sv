# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        stack=[]
        result =[]
        head=reversed(head)
        while head !=None:
            if len(stack)==0:
                result.append(0)
                stack.append(head.val)
                head=head.next
            elif stack[-1] > head.val:
                result.append(stack[-1])
                stack.append(head.val)
                head=head.next
            else:
                stack.pop()
        result=reversed(result)
        return result













        # stack=[]
        # if len(stack)==0:
        #     stack.append(head[len(head))
        #     head[len(head)]=0
        # len(head) -=1
        # while stack[-1] < head[len(head)]:
        #     stack.pop()
        # head[len(head)]=stack.top()
        # stack.append(head[len(head)])
        








        # pre = curr = head
        # arr=[]
        # while curr:
        #     while curr.next and curr.val <= pre.val:
        #         curr=curr.next
        #     if curr.val > pre.val:
        #         arr.append(curr.val)
        #         pre=pre.next
        #         curr = pre.next
        #     else:
        #         arr.append(0)
        # return arr