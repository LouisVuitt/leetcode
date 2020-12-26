class Solution(object):
    def shuffle(self,nums, n):
        x = []
        y = []
        ans = []
        for i in range(n):
            x.append(nums[i])
            y.append(nums[n+i])
        for i in range(n):
            ans.append(x[i])
            ans.append(y[i])
        return ans