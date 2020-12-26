class Solution(object):
    def findMagicIndex(self, nums):
        ans = -1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == i:
                ans = i
        return ans