class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalSum=nums[0]
        currentSum=nums[0]
        for i in nums[1:]:
           currentSum=max(i,currentSum+i)
           globalSum=max(globalSum,currentSum)
        return  globalSum