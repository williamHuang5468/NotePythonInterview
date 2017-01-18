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
