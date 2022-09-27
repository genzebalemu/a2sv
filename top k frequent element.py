class Solution(object):
    def topKFrequent(self, nums, k):
        list=[]
        N=len(nums)
#         this makes the list to dictionary
        mp = {}
        for i in range(N):
            if nums[i] in mp:
                mp[nums[i]] += 1
            else:
                mp[nums[i]] = 1
#         a is an array zero and it will be modified
        a = [0] * (len(mp))
        j = 0
#         it sets list of lists(key valeue with there frequency)
        for i in mp:
            a[j] = [i, mp[i]]
            j += 1
# it sorts the array in reverse order     
        a = sorted(a, key=lambda x: x[1],
               reverse=True)
#   append the key value to the list in k rangea and then print it
        for i in range(k):
            list.append(a[i][0])
        return list