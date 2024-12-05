class Solution(object):
    def minSubArrayLen(self, target, nums):
        #  7 [2,3,1,2,4,3]
        #         l   r
        l = 0
        r = 1
        sums = 0
        count = float('inf')

        for r in range(len(nums)):
            sums += nums[r]
            while sums >= target:
                count = min(r - l + 1, count)
                sums -= nums[l]
                l += 1
                
            r += 1
        if count == float('inf'):
            return 0
        else: 
            return count
        


        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        