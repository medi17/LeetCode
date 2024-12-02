class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        # sentence = "i love eating burger", searchWord = "burg"
        # Output: 4
        s = sentence.split(" ")

        for i, j in enumerate(s):
            if j.startswith(searchWord):
                return i + 1
        return -1



        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        