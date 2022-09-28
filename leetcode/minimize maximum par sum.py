class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        lower = 0
        upper = len(nums)-1
        res = 0
        while lower < upper: 
            res = max( res, (nums[lower] + nums[upper]))
            lower += 1
            upper -= 1
        return res