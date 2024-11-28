class Solution(object):
    def runningSum(self, nums):
        result = []
        sums = 0
        for num in nums:
            sums += num
            result.append(sums)  
        return result





        """
        :type nums: List[int]
        :rtype: List[int]
        """
        