class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre= [1]*(n+1)
        suf = [1]*(n+1)
        for i in range(1,n):
            pre[i] = pre[i-1]*nums[i-1]
        
        for i in range(n-1,0,-1):
            suf[i] = suf[i+1]*nums[i]
        
        output = []
        for i in range(n):
            output.append(pre[i]*suf[i+1])
        return output