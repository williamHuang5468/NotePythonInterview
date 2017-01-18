# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        headNode = head
        if headNode:
            position = 1
        else:
            position = 0

        prv = None
        isRevese = False
        while(headNode):
            if position is 1 and m is n :
                return headNode

            if position is m:
                isRevese = True
            if isRevese:
                twoP = prv
                prv = headNode
                headNode = headNode.next
                prv.next = twoP
            
        headNode = prv
        return headNode
