class Solution(object):
    def maxArea(self, height):
        if len(height) < 2:
            return 0
        i, j = 0, len(height)-1
        res = float("-inf")
        def getArea(i,j):
            if height[i] < height[j]:
                return (j - i) * height[i]
            else:
                return (j - i) * height[j]
        while i < j:
            area = getArea(i,j)
            res = max(res, area)
            if height[i] < height[j]:
                left = height[i]
                i = i + 1
                while i <= j and height[i] <= left:
                    i= i + 1
            else:
                right = height[j]
                j = j - 1
                while i <= j and height[j] <= right:
                    j = j - 1
        return res