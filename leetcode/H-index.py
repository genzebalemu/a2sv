class Solution(object):
    def hIndex(self, citations):
        if len(citations) ==0:
            return 0
        citations.sort()
        ans =len(citations)
        result=0
        for i in range(len(citations)):
            ans = min(citations[i], len(citations) - i)
            result = max(ans, result)
        
        return result