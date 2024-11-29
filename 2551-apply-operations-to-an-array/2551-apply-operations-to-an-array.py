class Solution(object):
    def applyOperations(self, nums):
        # [1,2,2,1,1,0]
        #  i = 0: nums[0] != nums[1], so we skip this operation.
        #  i = 1: nums[1] = nums[2] ,  nums[1] * 2 and nums[2] = 0. 
        #  [1,4,0,1,1,0]


        for i in range(len(nums)-1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i]*2
                nums[i + 1] = 0
        
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)

        return nums



        """
        :type nums: List[int]
        :rtype: List[int]
        """
        