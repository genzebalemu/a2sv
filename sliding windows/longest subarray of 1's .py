class Solution(object):
    def longestSubarray(self, nums):
        k=1
        j=0
        res =0
        for i in range(len(nums)):
            if nums[i]==0:
                k -=1
            while k < 0:
                if nums[j]==0:
                    k +=1
                j +=1
            res= max(res,i-j)
        return res