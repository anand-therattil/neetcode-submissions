class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # m = len(nums1)
        # n = len(nums2)

        # n1, n2 = 0,0 
        # final_array= [] 
        # left = 0 
        # right = 0 

        # while left <m and right <n:
        #     if nums1[left]<= nums2[right]:
        #         final_array.append(nums1[left])
        #         left+=1

        #     else:
        #         final_array.append(nums2[right])
        #         right+=1     
                
            
        # while left <m:
        #     final_array.append(nums1[left])
        #     left +=1 
        
        # while right<n:
        #     final_array.append(nums2[right])
        #     right +=1 

        # print(final_array)
        # if (m+n)%2 :
        #     return final_array[(m+n)//2]
        # else:
        #     return (final_array[(m+n)//2 -1] +final_array[(m+n)//2 ])/2
            

        if len(nums1)>len(nums2):
             nums1,nums2 = nums2,nums1
                
        m = len(nums1)
        n = len(nums2)
        
        low = 0 
        high = m

        while low<=high :

            part1 = (low+high)//2
            part2 = (m+n+1)//2 - part1

            maxleft1 = float("-inf") if part1 ==0 else nums1[part1-1]
            minright1 = float("inf") if part1 ==m else nums1[part1]

            maxleft2 = float("-inf") if part2 ==0 else nums2[part2-1]
            minright2 = float("inf") if part2 ==n else nums2[part2]

            if maxleft1 <= minright2 and maxleft2 <=minright1:
                if (m+n)%2:
                    return float(max(maxleft1, maxleft2))
                else:
                    return (max(maxleft1, maxleft2) +min(minright1, minright2)) / 2
            elif maxleft1>minright2:
                high = part1-1
            else:
                low = part1+1

                
