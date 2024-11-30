class Solution(object):
    def moveZeroes(self, nums):
        # [0,1,0,3,12]
        #  l r
        # [1,3,12,0,0,0]
        #      l      r
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
        return nums
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        