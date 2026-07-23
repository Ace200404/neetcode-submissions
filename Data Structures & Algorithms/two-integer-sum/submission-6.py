class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for curr in range(len(nums)):
            for nxt in range(curr+1,len(nums)):
                if nums[curr]+nums[nxt]== target:
                    return [curr,nxt]