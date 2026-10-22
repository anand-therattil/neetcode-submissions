class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_brac = {"}":"{", "]":"[", ")":"(" }
        for i in s:
            if i in map_brac:
                if not stack or stack.pop() !=map_brac[i]:
                    return False
            else:
                stack.append(i)
        
        return not stack
