from collections import defaultdict
class Solution:
    def check_anagram(self, s, t):
        n,m = len(s),len(t)
        if n!= m:
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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # n = len(strs)
        # visited = [False]*n
        # output = [] 
        # for i in range(n):
        #     if visited[i]==True:
        #         continue
        #     visited[i] = True
        #     temp = [strs[i]]
        #     for j in range(i+1,n):
        #         if not visited[j] and self.check_anagram(strs[i],strs[j]):
        #             temp.append(strs[j])
        #             visited[j]=True
        #     output.append(temp)
        # return output
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for ch in s:
                count[ord(ch) - ord('a')] += 1

            groups[tuple(count)].append(s)

        return list(groups.values())


            
                