class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        new = [True]*len(r)
        for i in range(len(r)):
            data = nums[l[i]:r[i]+1]
            data.sort()
            d = []
            for j in range(len(data) - 1):
                d.append(data[j+1] - data[j])
                d = list(set(d))
            if len(d) != 1:
                new[i] = False
        return new