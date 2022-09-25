class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        ans = 0
        while(len(piles)!=0):
            ans = ans + piles[-2]
            del piles[-2]
            del piles[-1]
            del piles[0]
        return ans