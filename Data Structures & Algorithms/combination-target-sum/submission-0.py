class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res,sol=[],[]
        n=len(nums)

        def dfs(i):
            if sum(sol)==target:
                res.append(sol[:])
                return
            if i>=n or sum(sol)>target:
                return
            
            dfs(i+1)

            sol.append(nums[i])
            dfs(i)
            sol.pop()

        dfs(0)
        return res