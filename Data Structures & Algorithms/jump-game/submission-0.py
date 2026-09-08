class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump=0

        for distance in nums:
            if jump<0:
                return False
            elif distance>jump:
                jump=distance
            jump-=1
        return True