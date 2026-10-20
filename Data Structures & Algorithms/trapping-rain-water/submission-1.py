class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height) 
        max_area = 0 
        # for curr in range(n):
        #     area = 0 
        #     left = curr - 1 
        #     right = curr + 1

        #     max_left  = 0 
        #     max_right = 0 
        #     while left >=0:
        #         max_left = max(max_left, height[left])
        #         left -=1
        #     while right <n:
        #         max_right = max(max_right, height[right])
        #         right += 1 
            
        #     area = min(max_left, max_right) - height[curr]
        #     max_area += max(area,0)
        # return max_area
        left_max, right_max = 0, 0 
        left= 0 
        right = n-1
        total = 0
        while left<right :
            if height[left]<=height[right]:
                if left_max <= height[left]:
                    left_max = height[left]
                else:
                    total+= left_max - height[left]
                left +=1
            else:
                if right_max <= height[right]:
                    right_max = height[right]
                else:
                    total+= right_max - height[right]
                right -=1

        return total

