class Solution(object):
    def swapNumbers(self, numbers):
        numbers = numbers * 2
        del numbers[0]
        del numbers[-1]
        return numbers