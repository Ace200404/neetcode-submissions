class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

            max_val=nums[0]
            curr_val=nums[0]

            for i in nums[1:]:

                curr_val=max(i, curr_val+i)

                max_val = max(max_val, curr_val)
            
            return max_val