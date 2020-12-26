class Solution(object):
    def sortedSquares(self, nums):
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i]**2)
        ans.sort()
        return ans