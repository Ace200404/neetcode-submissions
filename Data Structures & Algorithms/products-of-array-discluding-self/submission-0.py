class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rt = [1]* len(nums)

        prefix =1

        for i in range(len(nums)):
           rt[i]=prefix
           prefix= prefix*nums[i]
        postfix=1
        for j in range(len(nums)-1,-1,-1):
            rt[j]= postfix * rt[j]
            postfix = postfix*nums[j]
        return rt