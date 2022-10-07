class Solution(object):
    def findOriginalArray(self, changed):
        dic= collections.Counter(changed)
        list=[]
        if len(changed)==1:
            return []
        for i in sorted(changed):
            if dic[i]==0:
                continue
            if dic[2*i]==0:
                return []
            if i==0 and dic[i] <=1:
                return []
            list.append(i)
            dic[i] -=1
            dic[2*i] -=1
        return list
        
       