class Solution(object):
    def kthLargestNumber(self, nums, k):
        for i in range(len(nums)):
            nums[i]=int(nums[i])
        nums.sort()
        kthlargest= nums[len(nums)-k]
        return str(kthlargest)