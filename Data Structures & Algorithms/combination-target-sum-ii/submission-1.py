class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res,sol=[],[]

        candidates.sort()

        def dfs(startingIndex,currentTarget):
            
            if currentTarget==0:
                res.append(sol[:])
                return 
            
            if currentTarget<0:
                return
            
            for i in range(startingIndex,len(candidates)):
                if i>startingIndex and candidates[i]==candidates[i-1]:
                    continue
                
                sol.append(candidates[i])
                dfs(i+1,currentTarget-candidates[i])
                sol.pop()
        dfs(0,target)

        return res
