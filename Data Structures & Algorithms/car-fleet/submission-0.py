class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps =[]
        n = len(position)
        for i in range(n):
            ps.append((position[i],speed[i]))
        ps = sorted(ps, reverse=True)

        stack = [] 
        for i in range(n):
            stack.append((target-ps[i][0])/ps[i][1])
        
        
        fleet = 0
        mini = -1
        while stack:
            value = stack.pop(0)
            if value > mini :
                fleet +=1
                mini = value 
           
        return fleet
