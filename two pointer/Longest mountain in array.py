class Solution(object):
    def longestMountain(self, arr):
        # count =1
        res =0
        l=r=0
        
        for i in range(1,len(arr)-1):
            if arr[i]>arr[i+1] and arr[i]> arr[i-1]:
                l=r=i
                while l>0 and arr[l]>arr[l-1]:
                    l -=1
                while r+1<len(arr) and arr[r]>arr[r+1]:
                    r +=1  
                res=max(res,r-l+1)           
        return res   