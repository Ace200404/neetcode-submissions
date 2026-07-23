class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==0:
            return -1
        if len(nums)==1:
            return nums[0]
        subMax=nums[0]
        for left in range(len(nums)):
            currmax=0
            for right in range(left,len(nums)):
                currmax+=nums[right]
                print(currmax)
                subMax=max(subMax,currmax)
        return subMax