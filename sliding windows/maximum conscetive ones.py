class Solution(object):
    def longestOnes(self, nums, k):
        l=ones=zero=0
        for r in range(len(nums)):
            if nums[r] ==0:
                zero +=1
            if zero > k:
                if nums[l]==0:
                    zero -=1     
                l +=1
            ones = max(ones,r-l+1)
        return ones