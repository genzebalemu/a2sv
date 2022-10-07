class Solution(object):
    def maxVowels(self, s, k):
        max_vowel=0
        res =0
        for i in range(0,len(s)):
            if i>=k :
                if s[i-k] in "aeiou":
                    res -=1
            if s[i] in "aeiou":
                res+=1
            max_vowel = max(max_vowel,res)
        return max_vowel