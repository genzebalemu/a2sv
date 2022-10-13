class Solution(object):
    def rotate(self, nums, k):
        if len(nums) <= k:
            m=0
            i=len(nums)-1
            while m<i:
                nums[m] = nums[i]
                i -=1
                m +=1
            return nums
        temp=[0]*len(nums)
        j=0
        for i in range(len(nums)-k,len(nums)):
            temp[j] = nums[i]
            j +=1
            
        for l in range(len(nums)-k):
            temp[j] = nums[l]
            j +=1
        
        for m in range(len(nums)):
            nums[m] = temp[m]
        
        return temp 
        