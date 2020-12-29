class MinStack(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append((x,x))
            return
        
        currentMin = self.stack[-1][1]
        self.stack.append((x,min(x,currentMin)))

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
        
stack = MinStack()


minStack = MinStack();
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
minStack.top()
print(minStack.getMin())