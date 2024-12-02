class Solution(object):
    def threeSum(self, nums):
        total = []
        nums.sort()
        for i in range(len(nums) - 1):
            l = i + 1
            r = len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                if nums[l] + nums[r] + nums[i] == 0:
                    total.append([nums[l], nums[r], nums[i]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[l] + nums[r] + nums[i] < 0:
                    l += 1
                else:
                    r -= 1
        return total




        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        