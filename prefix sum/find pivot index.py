class Solution(object):
    def pivotIndex(self, nums):
        sum = 0;
        for i in nums:
            sum += i
        temp = 0
        for i in range(len(nums)):
            sum -= nums[i]
            if(temp == sum):
                return i
            temp += nums[i]
        return -1