class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        kv = {}
        for i in range(len(nums)):
            if nums[i] in kv.keys():
               kv[nums[i]] +=[i] 
            else:
                kv[nums[i]]= [i]

        print(kv)
        for i in range(len(nums)):
            left = target - nums[i]
            if left in kv.keys():
                print(f"{left}")
                print(f"{nums[i]}")
                if left == nums[i]:
                    if len(kv[nums[i]])>1:
                        return [i,kv[nums[i]][1]]
                else:
                    return [i,kv[left][0]]



