class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.res=[]
        self.backtrack([],nums,[False]*len(nums))
        return self.res
    def backtrack(self,perm,nums,numList):
        if len(perm)==len(nums):
            self.res.append(perm[:])
        for i in range(len(nums)):
            if not numList[i]:
                perm.append(nums[i])
                numList[i]=True
                self.backtrack(perm,nums,numList)
                perm.pop()
                numList[i]=False
