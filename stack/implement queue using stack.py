class MyQueue(object):
    def __init__(self):
        self.s1=[]
        self.s2=[]  
    def push(self, x):
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop()) 
            
        self.s1.append(x)
        
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())       
    def pop(self):
        return self.s1.pop()
    def peek(self):
        return self.s1[-1]
    def empty(self):
        if len(self.s1)+len(self.s2)==0:
            return True
        else:
            return False
        
