class Solution(object):
    def moveZeroes(self, nums):
        l=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[l] =nums[i]
                l +=1
        for j in range(l,len(nums)):
            nums[j]=0    
        return nums 
        
#         j = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[j], nums[i] = nums[i], nums[j] 
#                 j += 1
#         return nums 
                        
             