class Solution(object):
    def validateStackSequences(self, pushed, popped):
        self.stack=[]
        j=0
        n=len(pushed)
        for i in pushed:
            self.stack.append(i)
            while len(self.stack)!=0 and self.stack[-1] == popped[j]:
                self.stack.pop()
                j +=1
        return j == n