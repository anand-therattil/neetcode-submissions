class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for i in nums:
            if i in hm:
                return True
            hm[i]=True
            
        return False 