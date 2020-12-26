class Solution(object):
    def moveZeroes(self, nums):
        zero_index = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_index.append(i)
        for i in range(len(zero_index)):
            del nums[zero_index[i]-i]
        for i in range(len(zero_index)):
            nums.append(0)
        return nums