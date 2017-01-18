class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue(object):
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        data = self.front.data
        self.front = self.front.next
        return data

    def isEmpty(self):
        return self.front is None

if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(3)
    print("{} is 5 ".format(q.dequeue()))
    print("{} is 3 ".format(q.dequeue()))
    print("{} is True ".format(q.isEmpty()))
