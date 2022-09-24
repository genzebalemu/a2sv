class Solution(object):
    def sortSentence(self, s):
        temp = s.split()
        word={}
        ans=''
        for i in temp:
            word[i[-1]] = i[:-1]
        for i in sorted(word):
            ans=ans+''.join(word[i])+' '
        ans=ans[:-1]
        return ans
#         temp =s.split()
#         for i in range(len(temp)):
#             for j in range(len(temp)-1):
#                 if temp[j][-1] > temp[j+1][-1]:
#                     temp[j],temp[j+1] = temp[j+1],temp[j] 
                    
#         for i in range(len(temp)):
#             temp[i].remove(temp[i][-1])
#             ans= ans+''.join(temp[i])+' '
        
#         return ans