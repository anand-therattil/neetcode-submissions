class Solution:
    def twoSum(self, number: List[int], target: int) -> List[int]:
        i, j = 0, len(number) - 1

        while i < j:
            summ = number[i] + number[j]
            if summ > target:
                j -= 1
            elif summ < target:
                i += 1
            else:
                return [i + 1, j + 1]
        

        