class Solution(object):
    def maximum(self, a, b):
        ans = []
        ans.append(a)
        ans.append(b)
        ans.sort(reverse = True)
        return ans[0]