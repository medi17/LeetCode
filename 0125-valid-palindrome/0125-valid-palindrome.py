class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        return s == s[::-1]
        
        """
        :type s: str
        :rtype: bool
        """
        