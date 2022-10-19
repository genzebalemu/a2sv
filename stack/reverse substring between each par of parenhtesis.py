class Solution(object):
    def reverseParentheses(self,s):
        stack=[]
        temp=0
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            else :
                if s[i] == ")":
                    temp = s[stack[-1]:i + 1]
                    s = s[:stack[-1]] + temp[::-1] + s[i + 1:]
                    del stack[-1]
        ans =""
        for i in range(len(s)):
            if s[i] != ")" and s[i] != "(":
                ans += (s[i])
            
        return ans 