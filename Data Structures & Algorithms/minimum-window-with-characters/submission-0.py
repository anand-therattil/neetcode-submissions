import string

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        n= len(s)
        m = len(t)
        hm = {char:0 for char in string.ascii_letters}
        for i in t:
            hm[i] +=1

        l = 0
        r = 0 
        min_len = float("inf")
        count =0 
        start_index = -1 

        while l<=r and r<n:
            if hm[s[r]]>0:
                count+=1
            hm[s[r]]-=1
            while count == m:
                if  r-l+1 <min_len:
                    min_len = r-l+1  
                    start_index = l 
                hm[s[l]]+=1
                if hm[s[l]]>0:
                    count -=1 
                l+=1

                    
                
            r +=1 


        if start_index ==-1:
            return ""
        else:
            return s[start_index:start_index+min_len] 
        