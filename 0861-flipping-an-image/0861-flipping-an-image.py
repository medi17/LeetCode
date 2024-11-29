class Solution(object):
    def flipAndInvertImage(self, image):
        # brute force
        # [[1,1,0],[1,0,1],[0,0,0]]
        # i = 0   image[0] = [1, 1, 0]
        images2 =[]
        for i in range(len(image)):
            images = image[i][::-1]
            for j in range(len(images)):
                if images[j] == 0:
                    images[j] = 1
                elif images[j] == 1:
                    images[j] = 0
            images2.append(images)
        return images2
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        