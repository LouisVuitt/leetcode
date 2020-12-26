class Solution(object):
    def subtractProductAndSum(self, n):
        plus = 0
        multiply = 1
        ans = 0
        s = []
        while n>=10:
            s.append(n % 10)
            n = n / 10
            n = int(n)
        s.append(n)
        for i in range(len(s)):
            plus = plus + s[i]
            multiply = multiply * s[i]
        return multiply-plus