class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums= set(nums)
        curr=None
        longest=1
       
        for num in nums:
            if num-1 not in nums:
                curr = num
                streak=1
                while curr+1 in nums:
                    curr+=1
                    streak+=1
                
                longest= max(longest, streak)
        return longest
