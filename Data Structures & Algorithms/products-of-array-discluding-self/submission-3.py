class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        lst=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            lst[i]=prefix
            prefix= prefix*nums[i]

        postfix=1

        for i in range(len(nums)-1,-1,-1):
            lst[i]= lst[i]*postfix
            postfix= postfix*nums[i]
            
        
        return lst

