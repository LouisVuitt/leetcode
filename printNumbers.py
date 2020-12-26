class Solution(object):
    def printNumbers(self, n):
        ans = []
        for i in range(10**n):
            ans.append(i)
        del ans[0]
        return ans