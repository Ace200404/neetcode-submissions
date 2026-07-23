class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dub_num={}

        for i in nums:
            if i in dub_num:
                return True
            dub_num[i]=1
        return False