class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack(object):
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)

        prv = cur = self.top
        while(cur and cur.data < data):
            prv = cur
            cur = cur.next

        new_node.next = cur
        if cur is self.top:
            self.top = new_node
        else:
            prv.next = new_node

    def pop(self):
        if self.isEmpty():
            return -1
        value = self.top.data
        self.top = self.top.next
        return value

    def isEmpty(self):
        return self.top is None


if __name__ == "__main__":
    q = Stack()
    q.push(5)
    q.push(3)
    q.push(7)
    print("{} is 3 ".format(q.pop()))
    print("{} is 5 ".format(q.pop()))
    print("{} is 7 ".format(q.pop()))
