class Solution(object):
    def sortedSquares(self, nums):
        l = 0
        r = len(nums) - 1
        numbers = [] 

        while l <= r:
            if abs(nums[r]) < abs(nums[l]):
                numbers.append(nums[l] ** 2)
                l += 1
            else:
                numbers.append(nums[r] ** 2)
                r -= 1

        numbers.reverse()

        return numbers
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        