class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index={}
        for i, num in enumerate(nums):
            compl = target-num
            if compl in index:
                return [index[compl],i]
            index[num]=i
        return False
            