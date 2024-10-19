class Solution(object):
    def twoSum(self, nums, target):

        list1 = {}

        for i,j in enumerate(nums):
            if target - j in list1:
                return([list1[target - j], i])
            elif j not in list1:
                list1[j] = i
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        