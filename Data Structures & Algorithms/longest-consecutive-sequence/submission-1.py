class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = {}
        
        # for i in range(len(nums)):
        #     if nums[i] not in hm:
        #         hm[nums[i]]= [] 
        #     hm[nums[i]].append(i) 
        # # print(hm)
        # max_len= 0
        # for i in nums:
        #     a = i 
        #     length = 0
        #     while a in hm:
        #         length +=1
        #         a +=1
        #     # print(length,max_len)
        #     max_len = max(max_len,length)
            
        # return max_len
        hm = set(nums)
        max_len = 0
        for i in hm:
            if i-1 not in hm:
                length = 1
                while i + length in hm:
                    length+=1
                max_len = max(length, max_len)
        return max_len

        

