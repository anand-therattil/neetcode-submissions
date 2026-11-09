class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix), len(matrix[0])
        row= 0 
        column =0 

        for i in range(r):
            if matrix[i][0]<=target and target<=matrix[i][-1]:
                row = i
                break 
        low = 0 
        high = c
        while low <high:
            mid = (low+high )//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]<target:
                low = mid +1 
            else:
                high = mid
        return False
