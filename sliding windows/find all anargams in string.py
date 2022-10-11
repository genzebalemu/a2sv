class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []
        hash_s ={}
        hash_p ={}
        for i in range(len(p)):
            hash_p[p[i]] =1 + hash_p.get(p[i],0)
            hash_s[s[i]] =1 + hash_s.get(s[i],0)
        
        if hash_p==hash_s:
            res=[0] 
        else:
            res= []
        l=0 
        for i in range(len(p),len(s)):
            hash_s[s[i]]  =1 + hash_s.get(s[i],0)
            hash_s[s[l]] -=1
            if hash_s[s[l]] ==0:
                hash_s.pop(s[l])
            l +=1
            if hash_s==hash_p:
                res.append(l)
        return res