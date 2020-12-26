class Solution(object):
    def kthFactor(self, n, k):
        ans = []
        for i in range(1,n+1,1):
            if n % i == 0:
                ans.append(i)
        if k > len(ans):
            return -1
        else:
            return ans[k-1]