class Solution(object):
    def chalkReplacer(self, chalk, k):
        total = 0
        for i in chalk:
            total += i
        remainder = k % total
        if remainder==0:
            return 0
        for i in range(len(chalk)):
            remainder -= chalk[i]
            if remainder < 0:
                return i