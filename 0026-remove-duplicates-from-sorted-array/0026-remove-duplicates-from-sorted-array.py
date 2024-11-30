class Solution:
    def removeDuplicates(self, nums):
        r = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[r] = nums[i]
                r += 1 
        return r        


        """
        :type nums: List[int]
        :rtype: int
        """
        