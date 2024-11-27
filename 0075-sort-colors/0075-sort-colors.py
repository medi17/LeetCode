class Solution(object):
    def sortColors(self, nums):
        # [2,0,2,1,1,0]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]> nums[j] :
                    nums[i], nums[j] = nums[j], nums[i]
        
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
        