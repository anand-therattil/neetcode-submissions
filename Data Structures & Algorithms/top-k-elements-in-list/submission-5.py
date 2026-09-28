import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        
        for i in range(len(nums)):
            if nums[i] not in hm:
                hm[nums[i]] = 0 
            hm[nums[i]] +=1 

        hq = []
        for key,count in hm.items():
            hq.append((-count,key))
        heapq.heapify(hq)
        output = []

        while k > 0:
            value = heapq.heappop(hq)
            output.append(value[1])
            k -= 1
        return output

            

            
        