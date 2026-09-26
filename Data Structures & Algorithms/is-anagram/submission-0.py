class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            kv = {}
            kv2 = {}
            for i in s:
                if i not in kv.keys():
                    kv[i]=1
                else:
                    kv[i] +=1

            for i in t:
                if i not in kv2.keys():
                    kv2[i]=1
                else:
                    kv2[i] +=1
            if kv==kv2:
                return True
            else:
                return False