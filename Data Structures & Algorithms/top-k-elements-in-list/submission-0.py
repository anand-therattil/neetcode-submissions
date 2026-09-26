from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = defaultdict(list)
        kv = {}
        for i in nums:
            if i  not in kv.keys():
                kv[i] = 1
            else:
                kv[i] +=1

        for i,j in kv.items():
            result[j].append(i)
        
        max_value = sorted(result.keys(),reverse=True)
        
        output = []
        for i in max_value:
            output += list(result[i])
            if len(output)==k:
                break
        print(output)
        return output


        



