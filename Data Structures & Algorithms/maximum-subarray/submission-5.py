class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==0:
            return -1
        if len(nums)==1:
            return nums[0]
        max_so_far=nums[0]
        max_right_now=nums[0]

        for i in nums[1:]:

            max_right_now=max(i, max_right_now+i)
            max_so_far=max(max_right_now,max_so_far)
            
        return max_so_far