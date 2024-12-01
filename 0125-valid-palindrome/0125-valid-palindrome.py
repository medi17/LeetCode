class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        
        """
        :type s: str
        :rtype: bool
        """
        