

class Stack(object):
    '''
    using linked list to impment the Stack.
    '''
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        data = self.top.data
        self.top = self.top.next
        return data

    def isEmpty(self):
        return self.top is None


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
