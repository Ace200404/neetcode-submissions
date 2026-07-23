class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        st= sorted(set(nums))
        streak=1
        longest=1
        for i in range(1,len(st)):
            if st[i]== st[i-1]+1:
                streak+=1
                longest=max(longest,streak)
            else:
                streak=1
        return longest

        