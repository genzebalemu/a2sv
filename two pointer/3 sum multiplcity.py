class Solution(object):
    def threeSumMulti(self, arr, target):
        res=0
        hash=collections.Counter(arr)
        k=0
        for i in hash:
            for j in hash:
                k=target-i-j
                if k in hash:
                    if i==j and j==k:
                        res += (hash[i]*(hash[i]-1)*(hash[i]-2))/6
                    elif i ==j and j!=k:
                        res +=(hash[i]*(hash[i]-1)*hash[k])/2
                    elif i <j and j < k:
                        res+=hash[i]*hash[j]*hash[k]
                res =res%1000000007
        return res