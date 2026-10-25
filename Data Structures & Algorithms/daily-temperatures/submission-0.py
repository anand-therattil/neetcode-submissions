from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        
        n = len(temperatures)
        ptr = n-1
        output = [0]*n
        while ptr>=0:
            while stack and temperatures[stack[-1]]<=temperatures[ptr]:
                stack.pop()
            if stack:
                output[ptr] = stack[-1] - ptr
            stack.append(ptr)
            
            ptr-=1
        return output

