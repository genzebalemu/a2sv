class Solution(object): 
    def maxOperations(self, nums, k):
        map ={}
        result=0
        for i in nums:
            target = k-i
            if target in map and map[target] >0:
                result +=1
                map[target] -=1
            else:
                if i not in map:
                    map[i]=0
                map[i] +=1
        return result