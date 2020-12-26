class Solution(object):
    def countDigitOne(self, n):
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0: res = res + high * digit
            elif cur == 1: res = res + high * digit + low + 1
            else: res = res + (high + 1) * digit
            low = low + cur * digit
            cur = high % 10
            high = high / 10
            digit = digit * 10
        return res
