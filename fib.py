class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        f_0 = 0
        f_1 = 1
        f_n = 0
        for i in range(2, n+1):
            f_n = f_0 + f_1
            f_0 = f_1
            f_1 = f_n
        return f_n % 1000000007