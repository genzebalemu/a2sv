class Solution(object):
    def swap(self,nums,index1,index2):
        nums[index1],nums[index2]=nums[index2],nums[index1]
    def reverse(self,nums,start,end):
        while start<end:
            self.swap(nums,start,end)
            start +=1
            end -=1
    def nextPermutation(self, nums):
        if len(nums)==1:
            return nums
        if len(nums)==2:
            return self.swap(nums,0,1)
        last=len(nums)-2
        while last >=0 and nums[last] >= nums[last+1]:
            last -=1
        self.reverse(nums,last+1,len(nums)-1)
        if last ==-1:
            return nums 
        new_last =last+1
        while new_last<len(nums) and nums[new_last]<=nums[last]:
            new_last +=1
        self.swap(nums,new_last,last)
        
        
        
        



            





