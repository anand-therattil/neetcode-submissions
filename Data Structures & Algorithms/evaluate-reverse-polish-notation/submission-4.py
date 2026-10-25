from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        dq = deque()
        n = len(tokens)
        ptr = 0 

        while ptr<n:
            if tokens[ptr] not in ["+","-","*", "/"]:
                dq.append(int(tokens[ptr]))
            else:
                m = 0 
                a = dq.pop()
                b = dq.pop()
                if tokens[ptr] =="+":
                    dq.append(a+b)
                elif tokens[ptr] =="*":
                    dq.append(a*b)
                elif tokens[ptr] =="-":
                    dq.append(b-a)
                elif tokens[ptr] =="/":
                    dq.append(int(b/a))
            ptr+=1
        return dq[-1]
        