class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
        """
        Case 2
        reverseChar = [s[i] for i in range(len(s)-1, -1, -1)]
        reverseString = "".join(reverseChar)
        return reverseString
        """