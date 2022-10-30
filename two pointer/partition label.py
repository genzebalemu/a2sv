class Solution(object):
    def partitionLabels(self, s):
        res=[]
        hash={}
        end,size=0,0
        for i,char in enumerate(s):
            hash[char]=i
        for i,char in enumerate(s):
            size +=1
            end=max(end,hash[char])
            if i==end:
                res.append(size)
                size=0
        return res