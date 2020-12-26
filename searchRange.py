class Solution(object):
    def searchRange(self, nums, target):
        ans = []
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)
        if len(ans) == 0:
            return [-1,-1]
        if len(ans) == 1:
            return ans * 2
        if len(ans) == 2:
            return ans
        else:
            del ans[1:-1]
            return ans