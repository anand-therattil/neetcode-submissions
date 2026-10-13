class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi =0 
        i, j = 0, 0 
        n = len(prices)
        while i < n and j<n and i<=j:
            if prices[i]>=prices[j]:
                i = j 
                j+=1 
            elif prices[i]<prices[j]:
                maxi = max(maxi, prices[j]-prices[i])
                j+=1
        
        return maxi 