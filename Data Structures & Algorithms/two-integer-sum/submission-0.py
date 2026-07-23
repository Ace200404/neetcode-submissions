class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_nums={}

        for i, num in enumerate(nums):
            compl= target-num

            if compl in index_nums:
                return [index_nums[compl],i]
            
            index_nums[num]=i

        
        return False