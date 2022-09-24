class Solution(object):
    def targetIndices(self, nums, target):
        list=[]
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j] > nums[j+1]:
                    nums[j+1],nums[j] = nums[j],nums[j+1]
        for k in range(len(nums)):
            if nums[k] == target:
                list.append(k)
        return list