class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indecies={}
        for key,value in enumerate(nums):
            complement = target-value
            if complement in indecies:
                return [indecies[complement],key]
            indecies[value]=key
            