import unittest


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        '''
        Case1

        nums1 = [1, 3]
        nums2 = [2]

        The median is 2.0

        Case2

        nums1 = [1, 2]
        nums2 = [3, 4]

        The median is (2 + 3)/2 = 2.5
        '''
        num = sorted(nums1 + nums2)
        size = len(num)
        if size % 2 is 1:
            return num[size//2]
        else:
            mid = size//2
            return (num[mid-1] + num[mid]) / 2.0

class SolutionTest(unittest.TestCase):

    def testCase(self):
        nums1 = [1, 3]
        nums2 = [2]
        expected = 2
        self.assertEqual(Solution().findMedianSortedArrays
                         (nums1, nums2), expected)

    def testCase2(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        expected = 2.5
        self.assertEqual(Solution().findMedianSortedArrays
                         (nums1, nums2), expected)

if __name__ == '__main__':
    unittest.main()
