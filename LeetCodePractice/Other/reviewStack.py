class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack(object):
    '''
    0910, 用Linked List 實作 Stack
    '''
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        data = self.top.data
        self.top = self.top.next
        return data


class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node

    def reverse(self):
        cur = self.head
        prv = None
        while(cur):
            twoP = prv
            prv = cur
            cur = cur.next
            prv.next = twoP
        self.head = prv

    def visit(self):
        head = self.head
        while(head):
            print(head.data)
            head = head.next

    def insert(self, position, data):
        new_node = Node(data)
        head = self.head
        p = 1
        while(head):
            if p is position:
                new_node.next = head.next
                head.next = new_node
                return
            head = head.next


if __name__ == "__main__":
    q = Stack()
    q.push(5)
    q.push(3)
    print("{} is 3 ".format(q.pop()))
    print("{} is 5 ".format(q.pop()))

    L = LinkedList()
    L.add(3)
    L.add(5)
    L.visit()

    L.reverse()
    L.visit()

    L.insert(1,10)
    L.visit()
