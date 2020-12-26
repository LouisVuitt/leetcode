class Solution(object):
    def rotate(self, nums, k):
        nums_len = len(nums)
        num1 = nums[:nums_len-k]
        del nums[:nums_len-k]
        nums += num1