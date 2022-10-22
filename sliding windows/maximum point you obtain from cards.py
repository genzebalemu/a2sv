class Solution(object):
    def maxScore(self, cardPoints, k):
        l,r=0,len(cardPoints)-k
        total=sum(cardPoints[r:])
        res=total
        while r < len(cardPoints):
            total += cardPoints[l]-cardPoints[r]
            res=max(res,total)
            r +=1
            l +=1
        return res






            















