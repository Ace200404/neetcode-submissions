class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2)<len(nums1):
            nums1,nums2=nums2,nums1

        total=len(nums1)+len(nums2)
        half= total//2
        left,right=0,len(nums1)-1

        while True:
            middle1=(left+right)//2
            middle2=half-middle1-2

            left1=nums1[middle1] if middle1>=0 else float('-inf')
            right1=nums1[middle1+1] if (middle1+1)<len(nums1) else float('inf')
            left2=nums2[middle2] if middle2>=0 else float('-inf')
            right2=nums2[middle2+1] if (middle2+1)<len(nums2) else float('inf')
                
            if left1<=right2 and right1>=left2:    
                if total%2:
                    return min(right2,right1)
                return (max(left1,left2)+min(right1,right2))/2
            elif left1>right2:
                right=middle1-1
            else:
                left=middle1+1
