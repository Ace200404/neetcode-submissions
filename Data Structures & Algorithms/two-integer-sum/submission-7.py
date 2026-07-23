class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen={}

        for key, value in enumerate(nums):
            component = target - value
            if component in seen:
                return [seen[component], key]
            seen[value]=key