class MyQueue:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mainStack = []
        self.swapStack = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while len(self.mainStack) != 0:
            self.swapStack.append(self.mainStack.pop())
            
        self.mainStack.append(x)
        
        while len(self.swapStack) != 0:
            self.mainStack.append(self.swapStack.pop())
            
        print(self.mainStack)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.mainStack) > 0:
            return self.mainStack.pop()
        else:
            return None

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.mainStack) > 0:
            return self.mainStack[-1]
        else:
            return None

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.mainStack) == 0
        
stack = MyQueue()
stack.push(1)
stack.push(2)
print(stack.peek())
print(stack.pop())
stack.push(3)
print(stack.empty())