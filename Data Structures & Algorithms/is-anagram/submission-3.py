class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n!=m:
            return False

        hm = {}
        for i in s:
            if i not in hm:
                hm[i]=0
            hm[i]+=1
        for i in t:
            if i not in hm or hm[i]==0:
                return False
            hm[i]-=1
        return True
            