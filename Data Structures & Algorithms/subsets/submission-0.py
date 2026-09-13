class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result,solution=[],[]
        n=len(nums)
        def dfs(i):
            if i==n:
                result.append(solution[:])
                return
            dfs(i+1)
            
            solution.append(nums[i])
            dfs(i+1)
            
            solution.pop()


        dfs(0)
        return result