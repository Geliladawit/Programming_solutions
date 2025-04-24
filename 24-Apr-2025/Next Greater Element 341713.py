# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1 = len(nums1)
        n2 = len(nums2)
        res = []
        for i in range(n1):
            x = nums2.index(nums1[i])
            found = False
            for j in range(x+1,n2):
                if nums2[j] > nums1[i]:
                    res.append(nums2[j])
                    found = True
                    break
            if not found:
                res.append(-1)
        return res