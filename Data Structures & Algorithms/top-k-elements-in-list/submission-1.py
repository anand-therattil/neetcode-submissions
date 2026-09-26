from collections import defaultdict
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        temp = [[] for _ in range(len(nums) + 1)]
        for n, f in count.items():
            temp[f].append(n)
        output = []
        for i in range(len(temp)-1,-1,-1):
            print(temp[i])
            if temp[i]!=[]:
                output.extend(temp[i])
                if(len(output)>=k):
                    break
        print(output)
        return output
        
        
        
        
        
        
        
        
        
        
        # result = defaultdict(list)
        # kv = {}
        # for i in nums:
        #     if i  not in kv.keys():
        #         kv[i] = 1
        #     else:
        #         kv[i] +=1

        # for i,j in kv.items():
        #     result[j].append(i)
        
        # # max_value = sorted(result.keys(),reverse=True)
        
        # output = []
        # for i in max_value:
        #     output += list(result[i])
        #     if len(output)==k:
        #         break
        # print(output)
        # return output


        



