class Solution(object):
    def runningSum(self, nums):
        result = [nums[0]]
        sums = nums[0]
        for i in  range(1, len(nums)):
            sums += nums[i]
            result.append(sums)
            
        return result





        """
        :type nums: List[int]
        :rtype: List[int]
        """
        