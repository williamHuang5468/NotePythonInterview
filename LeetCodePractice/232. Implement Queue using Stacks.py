class Stack(object):
    def __init__(self):
        self._stack = []
    
    def push(self, value):
        self._stack.append(value)
    
    def pop(self):
        try:
            value = self._stack[-1]
            del self._stack[-1]
            return value
        except IndexError:
            print("is empty")
            
    def size(self):
        return len(self._stack)
    
    def top(self):
        return self._stack[0]

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = Stack()
        self.emptyStack = Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.push(x)

    def pop(self):
        """
        :rtype: nothing
        """
        while(self.stack.size() is not 1):
            self.emptyStack.push(self.stack.pop())
        value = self.stack.pop()
        self.stack, self.emptyStack = self.emptyStack, self.stack
        return value

    def peek(self):
        """
        :rtype: int
        """
        return self.stack.top()

    def empty(self):
        """
        :rtype: bool
        """
        return self.stack.size() is 0