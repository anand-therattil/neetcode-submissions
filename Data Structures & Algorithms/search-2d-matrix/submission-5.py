class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix), len(matrix[0])
        row= 0 
        column =0 

        # for i in range(r):
        #     if matrix[i][0]<=target and target<=matrix[i][-1]:
        #         row = i
        #         break 
        # low = 0 
        # high = c
        # while low <high:
        #     mid = (low+high )//2
        #     if matrix[row][mid]==target:
        #         return True
        #     elif matrix[row][mid]<target:
        #         low = mid +1 
        #     else:
        #         high = mid
        # return False
        if not matrix or not matrix[0]:
            return False
        low = 0 
        high = r*c -1 
        while low<=high :
            mid = (low+high)//2
            row= mid//c
            column = mid%c
            
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                low = mid + 1 
            else:
                high = mid-1
        return False

        

            
