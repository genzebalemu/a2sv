class Solution(object):
    def chalkReplacer(self, chalk, k):
        for i in chalk:
            if k >= i:
                k -=1
            else:
                return chalk.index(i)