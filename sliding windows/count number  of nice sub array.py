class Solution(object):
    def numberOfSubarrays(self, nums, k):
        count =0
        l=0
        ans =0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        for j in range(len(nums)):
            count +=nums[j]
            if count ==k:
                if nums[l]==1:
                    count -=1
                ans +=1
                l+=1
        return ans
        