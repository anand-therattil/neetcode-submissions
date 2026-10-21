import string 

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0 
        freq_map = {char: 0 for char in string.ascii_uppercase}
        n = len(s)
        left = 0 
        right = 0 
        max_freq =0 
        for right in range(n):
            freq_map[s[right]]+=1
            window_length = right - left + 1
            max_freq = max(max_freq, freq_map[s[right]])
            condition =  window_length - max_freq <= k 
            if condition: 
                max_len = max(max_len, window_length)
            else:
                freq_map[s[left]]-=1
                left +=1 
            

        return max_len
