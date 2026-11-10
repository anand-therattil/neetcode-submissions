class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        n1, n2 = 0,0 
        final_array= [] 
        left = 0 
        right = 0 


        while left <m and right <n:
            if nums1[left]<= nums2[right]:
                final_array.append(nums1[left])
                left+=1

            else:
                final_array.append(nums2[right])
                right+=1     
                
            
        while left <m:
            final_array.append(nums1[left])
            left +=1 
        
        while right<n:
            final_array.append(nums2[right])
            right +=1 

        print(final_array)
        if (m+n)%2 :
            return final_array[(m+n)//2]
        else:
            return (final_array[(m+n)//2 -1] +final_array[(m+n)//2 ])/2
            
            


                
