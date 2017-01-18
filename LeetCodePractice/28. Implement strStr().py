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
