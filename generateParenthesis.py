class Solution(object):
    def generateParenthesis(self, n):
        if n == 0:
            return []

        pre = ['()', ]
        for i in range(n - 1):
            now = set()
            for st in pre:
                n = len(st)
                for index in range(n):
                    now.add(st[:index] + '()' + st[index:])
            pre = now
        return list(pre)