                          
class Solution(object):
    def subarraySum(self, nums, k):
        ans = 0
        sum = 0
        map = {}
        map[0] = 1
        for n in nums:
            sum += n
            if sum - k in map:
                ans += map[sum - k]
            map[sum] = map.get(sum, 0) + 1
        return ans