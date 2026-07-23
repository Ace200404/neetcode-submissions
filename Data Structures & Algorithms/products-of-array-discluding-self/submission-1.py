class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result=[]
        for i in range(len(nums)):
            product=1
            for x in range(len(nums)):
                if i!=x:
                    product*=nums[x]
            result.append(product)
        return result