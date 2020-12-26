class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        while len(nums) > 2:
            del nums[0]
            del nums[-1]
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return (nums[0] + nums[1]) / 2.0
