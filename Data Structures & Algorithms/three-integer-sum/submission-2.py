class Solution:
    def two_sum(self, nums, target, index):
        i = index+1  
        j = len(nums)-1
        output = [] 
        while i < j :
            current_sum = nums[i] + nums[j]
            if current_sum +target == 0:
                output.append([target,nums[i],nums[j]])
                i+=1
                j-=1
                while i<j and nums[i]==nums[i-1]:
                    i+=1
                while i<j and nums[j]==nums[j+1]:
                    j-=1

            elif current_sum + target<0:
                i+=1
            elif current_sum + target>0:
                j-=1
        return output
            

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums= sorted(nums) #NlogN
        output = [] 
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i]
            output.extend(self.two_sum(nums,target, i))
        return output



        