import string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m= len(s2)
        if n>m:
            return False

        freq_map_s1 = {char:0 for char in string.ascii_lowercase}
        freq_map = {char:0 for char in string.ascii_lowercase}
        for i in s1:
            freq_map_s1[i]+=1

        left  = 0 
        right = 0 
        while left<=right and right < m:
            if right - left + 1< n:
                freq_map[s2[right]]+=1
                right+=1
            elif right - left + 1 ==n:
                freq_map[s2[right]]+=1
                if freq_map == freq_map_s1:
                    return True
                right+=1
            else:
                freq_map[s2[left]]-=1
                left+=1

        return False

