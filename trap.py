class Solution(object):
    def trap(self, height):
        n = len(height)
        s1, s2 = 0, 0
        max1, max2 = 0, 0
        for i in range(n):
            if height[i] > max1:
                max1 = height[i]
            if height[n - i - 1] > max2:
                max2 = height[n - i - 1]
            s1 += max1
            s2 += max2
        res = s1 + s2 - max1 * len(height) - sum(height)
        return res