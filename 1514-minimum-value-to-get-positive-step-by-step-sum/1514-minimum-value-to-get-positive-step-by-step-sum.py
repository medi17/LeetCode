class Solution(object):
    def minStartValue(self, nums):

        # [-3,2,-3,4,2]

        prefix_sum = 0
        start_value = 1

        for i in nums:
            prefix_sum += i 
            start_value = max(start_value, 1- prefix_sum)
            
        return start_value
    """
    :type nums: List[int]
    :rtype: int
    """
        