class Solution(object):
    def pivotIndex(self, nums):
       
        right_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum -= nums[i]

            if right_sum == left_sum:
                return i
            left_sum += nums[i]
        return -1
                
             
        """
        :type nums: List[int]
        :rtype: int
        """
        