class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        if len(tokens)== 0 or tokens[0]>power:
            return 0
        score =0
        right=len(tokens)-1
        left=0
        res=0
        while left<=right:
            if power>=tokens[left]:
                score +=1
                power -= tokens[left]
                left +=1
                res=max(res,score)
            else:
                if score>0:
                    score -=1
                    power +=tokens[right]
                    right -=1
                else:
                    break
        return res
        
