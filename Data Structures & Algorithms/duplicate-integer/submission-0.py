class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        kv= {}
        for i in nums:
            if i in kv.keys():
                return True
            else:
                kv[i] = 1
        return False


            
        