class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left=0 
        have={}
        need=Counter(t)
        formed=0
        min_length= float('inf')
        req_chars=len(need)
        result=''
        for right in range(len(s)):

            have[s[right]]= have.get(s[right],0)+1

            if s[right] in need and have[s[right]] == need[s[right]]:
                formed+=1
            
            while left <= right and formed == req_chars:

                if (right-left+1) < min_length:
                    min_length= right-left+1
                    result= s[left:right+1]
                
                have[s[left]]-=1

                if s[left] in need and have[s[left]] < need[s[left]]:
                    formed-=1
                left+=1
        return result
