# Leet Code

## 7. Reverse Integer

    Reverse digits of an integer.

    Example1: x = 123, return 321
    Example2: x = -123, return -321

```Python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            r = int(str(x)[:0:-1])
            if r > 2147483648:
                return 0
            else:
                return int("-" + str(r))
        else:
            r =  int(str(x)[::-1])
            if r > 2147483648:
                return 0
            else:
                return  r
```

## 9 isPalindromePalindrome Number  

```Python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        Case 1
        11506 / 11506 test cases passed.
        Runtime: 226 ms
        """
        if x < 0:
            return False
        else:
            value = str(x)

        for i in range(len(value)//2):
            if value[-(i+1)] != value[i]:
                return False
        return True


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        Case2
        11506 / 11506 test cases passed
        379 ms
        """
        if x < 0:
            return False
        else:
            value = str(x)
        result = self.isP(value)
        if result == []:
                return True
        else:
                return False
    def isP(self, value):
        return [False for i in range(len(value)//2) if (value[-(i+1)] != value[i])]
```


## 28 str Str

```Python
def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        
        72 / 72 test cases passed.
        Runtime: 49 ms
        """
        if needle == "" or haystack == needle:
            return 0
        size = len(needle)
        for i in range(len(haystack)-size+1):
                if haystack[i:i+size] == needle:
                        return i
        return -1
```



## 92. Reverse Linked List II

Linked List

Update:2016/0909，寫到一半，轉換的部份失敗

```Python


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

```

## 19. Remove Nth Node From End of List

### Notes

[1], 1 : []

[1,2], 1 : [1]

- 刪除節點
- 知道倒數第幾個
    - 總長
    - 倒數第幾個

