class Solution(object):
    def findNumbers(self, nums):
        ans = 0
        for i in range(len(nums)):
            s = str(nums[i])
            if len(s) % 2 == 0:
                ans = ans + 1
        return ans