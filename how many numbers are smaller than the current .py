class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        array = [0]* len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] > nums[j]:
                        array[i] +=1
                
        return array