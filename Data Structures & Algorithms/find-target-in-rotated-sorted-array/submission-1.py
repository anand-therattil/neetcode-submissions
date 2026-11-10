class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0 
        high= len(nums)-1

        while low < high :
            mid = (low+high)//2

            if nums[mid]>nums[high]:
                low =mid+1
            else:
                high = mid
        print(low,high)
        if target <= nums[low:][-1]:
            high = len(nums)-1
        else:
            high = low-1 
            low = 0
        print(low, high)
        
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid 
            elif nums[mid]<target:
                low = mid+1 
            else:
                high = mid-1
        
        return -1