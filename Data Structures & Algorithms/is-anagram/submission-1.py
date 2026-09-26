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
                if i not in kv.keys():
                    return False
                else:
                    if kv[i]==1:
                        kv.pop(i,None)
                    else:
                        kv[i] -=1
            if kv == {}:
                return True
            else:
                return False