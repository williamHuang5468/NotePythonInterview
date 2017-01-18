class Queue(object):
    """
    Implment Queue using List
    """
    def __init__(self):
        self._list = []
    
    def enqueue(self, value):
        self._list.append(value)
    
    def dequeue(self):
        try:
            value = self._list[0]
            del self._list[0]
            return value
        except IndexError:
            print("is empty")
    
    def size(self):
        return len(self._list)
    
    def top(self):
        if self.size() is 0:
            return 0
        return self._list[-1]

class Stack(object):
    def __init__(self):
        self.queue = Queue()
        self.emptyQueue = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.enqueue(x)

    def pop(self):
        """
        Put values of `queue` untail last one.
        """
        if self.queue.size() is 0:
            print("is empty")
            return
        
        while(self.queue.size() is not 1):
            self.emptyQueue.enqueue(self.queue.dequeue())
        value = self.queue.dequeue()
        self.queue, self.emptyQueue = self.emptyQueue, self.queue
        
        return value

    def top(self):
        """
        :rtype: int
        """
        return self.queue.top()

    def empty(self):
        """
        :rtype: bool
        """
        return self.queue.size() is 0
