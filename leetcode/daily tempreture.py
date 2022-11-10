class Solution(object):
    def dailyTemperatures(self, tempratures):
        n = len(tempratures)
        res = [0] * n 
        for i in range(n - 2, -1, -1):
            k = i + 1
            while tempratures[i] >= tempratures[k] and res[k] > 0:
                print(i)
                k += res[k]

            if tempratures[k] > tempratures[i]:
                res[i] = k - i
        return res
        