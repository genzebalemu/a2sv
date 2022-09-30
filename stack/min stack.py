class MinStack(object):
    def __init__(self):
        self.stack = []
    def push(self, value):
        if self.stack:
             self.stack.append(min(self.stack[-2], value))
        else:
            self.stack.append(value)
        self.stack.append(value)
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.stack.pop()
    def top(self):
        if self.stack:
            return self.stack[-1]
    def getMin(self):
        if self.stack:
            return self.stack[-2]