class Solution(object):
    def topKFrequent(self, nums, k):
        list=[]
        N=len(nums)
        mp = {}
        for i in range(N):
            if nums[i] in mp:
                mp[nums[i]] += 1
            else:
                mp[nums[i]] = 1
        a = [0] * (len(mp))
        j = 0
        for i in mp:
            a[j] = [i, mp[i]]
            j += 1     
        a = sorted(a, key=lambda x: x[1],
               reverse=True)
        for i in range(k):
            list.append(a[i][0])
        return list