class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        distinct = {}
        min_count = 0 
        max_count = 0 
        n = len(s)
        for i in range(n):
            if s[i] in distinct :
                min_count =  max(distinct[s[i]]+1,min_count)
                distinct[s[i]] = i
            else:
                distinct[s[i]] = i 
            max_count = max(max_count,  i-min_count+1)
            # print(min_count, max_count)
        return max_count 