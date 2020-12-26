class Solution(object):
    def smallestK(self, arr, k):
        arr.sort()
        del arr[k:]
        return arr