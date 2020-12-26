class Solution(object):
    def arrangeCoins(self, n):
        if n == 0:
            return 0
        value = 1
        while n >= value * 2 + 1:
            n = n - value
            value = value + 1
        return value