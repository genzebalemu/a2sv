class Solution(object):
    def maxFrequency(self, nums, k):
        N =len(nums)
        nums.sort()
        start = sum =end= res= 0
        for end in range(N):
            sum += nums[end]
            while ((end - start + 1) * nums[end] - sum > k):
                sum -= nums[start]
                start += 1
            res = max(res, end - start + 1)
        return res