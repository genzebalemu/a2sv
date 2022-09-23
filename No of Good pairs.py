class Solution(object):
    def numIdenticalPairs(self, nums):
        output = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j:
                    if nums[i] == nums[j]:
                        output +=1
        return output