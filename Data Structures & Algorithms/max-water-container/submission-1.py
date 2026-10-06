class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxa = 0
        i =0 
        j = len(heights)-1
        while i < j:
            maxa = max((j-i)*min(heights[i],heights[j]), maxa)
            # print(i,j, maxa)
            if heights[i]<=heights[j]:
                i+=1
            else:
                j-=1

        return maxa