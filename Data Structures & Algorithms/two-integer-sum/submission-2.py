class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            left = target - nums[i]
            if left in hm:
                return [hm[left],i]
            else:
                hm[nums[i]]= i

               