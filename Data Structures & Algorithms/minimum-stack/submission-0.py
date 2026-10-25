from collections import deque
class MinStack:

    def __init__(self):
        self.dq = deque()
        self.min = float("-inf")
        self.mini = deque()

    def push(self, val: int) -> None:
        self.dq.append(val)
        
        if not self.mini:
            self.mini.append(val)
        else:
            if self.mini[-1]<val:
                self.mini.append(self.mini[-1])
                
            else:
                self.mini.append(val)

    def pop(self) -> None:
        self.dq.pop()
        self.mini.pop()
    
    def top(self) -> int:
        return self.dq[-1]    

    def getMin(self) -> int:
        return self.mini[-1]


        
