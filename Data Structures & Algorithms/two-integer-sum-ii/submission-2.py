class Solution:
    def twoSum(self, number: List[int], target: int) -> List[int]:
        i=0 
        n =  len(number)
        j = n - 1 
        while i<j:
            summ = number[i]+number[j]
            if summ> target:
                j= j-1
            elif summ < target:
                i = i+1
            else:
                return [i+1,j+1] 