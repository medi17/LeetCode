class Solution(object):
    def addSpaces(self, s, spaces):
        m,n = len(spaces), len(s)
        word =[' ']*(m+n)
        r = 0
        for i, c in enumerate(s):
            if r < len(spaces) and  i == spaces[r]:
                r += 1 
            word[i+r]= s[i]

        return "".join(word) 


        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        