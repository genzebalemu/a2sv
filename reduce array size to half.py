class Solution(object):
    def minSetSize(self, arr):
        map = Counter(arr)
        ans = n = 0
        for _, i in map.most_common():
            n += i
            ans += 1
            if n * 2 >= len(arr):
                break
        return ans