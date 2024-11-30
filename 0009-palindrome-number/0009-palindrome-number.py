class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[r] == s[l]:
                l += 1
                r -= 1
            elif r!= l:
                return False
        return True


        """
        :type x: int
        :rtype: bool
        """

        