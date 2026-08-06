class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        
        while left<=right:
            root=(right+left)//2
            if nums[root]<target:
                left=root+1
            elif nums[root]>target:
                right=root-1
            else:
                return root
        return -1