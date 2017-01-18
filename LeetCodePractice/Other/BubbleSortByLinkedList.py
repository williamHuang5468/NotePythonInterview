class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def sort(self):
        cur = self.head
        twoP = None
        next = None
        prv = None
        while(cur):
            twoP = cur
            prv = twoP.next
            next = prv.next
            while(next):
                if(prv.data > next.data):
                    pass
                twoP = prv
                prv = next
                next = next.next
            cur = cur.next

    def visit(self):
        head = self.head
        while head:
            print(head.data)
            head = head.next


if __name__ == "__main__":
    q = LinkedList()
    q.add(3)
    q.add(7)
    q.add(5)
    q.sort()
    q.visit()
