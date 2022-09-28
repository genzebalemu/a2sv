class Solution(object):
    def evalRPN(self, tokens):
        stack = [] 
        for char in tokens:
            if char not in "+/*-":
                stack.append(int(char))
            else:
#                 pop the two elements in the top of the stack sequentially
                pop1,pop2 = stack.pop(), stack.pop()
    
                if char =="-":
                    stack.append(pop2-pop1)

                elif char=="+":
                    stack.append(pop2+pop1)

                elif char =="/":
                    stack.append(int(float(pop2)/pop1))
                    
                elif char == "*":
                    stack.append(pop1 * pop2)
   
        return stack[-1]