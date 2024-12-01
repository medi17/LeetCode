class Solution(object):
    def twoSum(self, numbers, target):
        # [2,7,11,15], target = 9

        r = len(numbers) - 1
        l = 0
        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l + 1, r + 1] 
        
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        