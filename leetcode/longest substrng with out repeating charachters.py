class Solution(object):
    def lengthOfLongestSubstring(self, s):
       
        hash={}
        max_len = 0
        start_idx = 0
        for i in range(len(s)):
            if s[i] in hash:
                start_idx = max(start_idx, hash[s[i]] + 1)
            max_len = max(max_len, i-start_idx + 1)   
            hash[s[i]] = i
        return max_len