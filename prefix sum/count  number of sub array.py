class Solution(object):
    def numberOfSubarrays(self, nums, k):
        list = []
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                list.append(i)
        start = 0
        end = k - 1
        i = 0
        count = 0
        while end < len(list):
            if end == len(list) - 1:
                j = len(nums) - 1
            else:
                j = list[end + 1] - 1
            count = count + (list[start] - i + 1) * (j - list[end] + 1)    
            i = list[start] + 1
            start = start + 1
            end = end + 1
        return count    
        
 