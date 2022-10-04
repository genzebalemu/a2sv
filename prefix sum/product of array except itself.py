class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        ans=[0]*n
        prefix=[0]*n 
        suffix = [0]*n
        prefix[0] = 1
        suffix[n - 1] = 1
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        for j in range(n-2,-1,-1):
            suffix[j] = nums[j + 1] * suffix[j + 1]
           
        for i in range(n):
            ans[i] = prefix[i] * suffix[i]
        return ans