

class List(object):
    def __init__(self, head):
        self.head = head

    def insertList(self, data):
        '''
        以小排到大的LinkedList
        '''
        new_node = Node(data)
        cur = prv = self.head
        while((cur is not None) and (cur.data < data)):
            prv = cur
            cur = cur.next
        new_node.next = cur
        if cur is self.head:
            self.head = new_node
        else:
            prv.next = new_node

    def addList(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def deleteList(self, data):
        cur = self.head
        while(cur and cur.data is not data):  # find the position of data
            prv = cur
            cur = cur.next
        if cur:  # find the data of position
            if cur is self.head:
                self.head = cur.next
            else:
                prv.next = cur.next

    def visitList(self):
        h = self.head
        while(h):
            print(h.data)
            h = h.next

    def reverseList(self):
        cur = self.head
        prv = None
        while(cur):
            twoPrv = prv
            prv = cur
            cur = cur.next
            prv.next = twoPrv  # Point to prv node
        self.head = prv

    def reverseListFromMToN(self, m, n):
        '''
        LeetCode#92
        '''
        cur = self.head
        prv = None
        position = 1
        isRevse = False
        while(cur):
            if position is m:
                isRevse = True
            if isRevse:
                twoPrv = prv
                prv = cur
                prv.next = twoPrv  # Point to prv node
            cur = cur.next
        self.head = prv


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class ListToTail(object):
    def __init__(self, head):
        self.head = head
        self.tail = head

    def addToTail(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
        self.tail = new_node

    def visitList(self):
        node = self.head
        while(node):
            print(node.data)
            node = node.next

if __name__ == '__main__':
    b = List(Node(5))
    b.addList(3)
    b.addList(8)
    # 8->3->5
    print("8->3->5 be 8->5->3")
    b.reverseListFromMToN(2, 3)
    b.visitList()
    # 8->5->3

    print("3->5 be 5->3")
    b = List(Node(3))
    b.addList(5)
    # 5 -> 3
    b.reverseListFromMToN(1, 2)
    b.visitList()
