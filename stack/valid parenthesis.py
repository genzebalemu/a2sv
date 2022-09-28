class Solution(object):
    def isValid(self,s):
        stack= deque()
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            else:
                if len(stack)==0 :
                    return False
                else:
                    open = stack.pop()
                    if i==')' and open !='(' or i==']' and open !='[' or i=='}' and open != '{':
                        return False
        return  len(stack) ==0 