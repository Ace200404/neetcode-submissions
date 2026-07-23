class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        have = {}
        need = Counter(t)
        required_chars = len(need)  
        formed = 0
        min_len = float('inf')
        result = ""

        for right in range(len(s)):
            # 1. Add s[right] to window
            have[s[right]] = have.get(s[right], 0) + 1
            
            # 2. Check if this char just reached its required count
            if s[right] in need and have[s[right]] == need[s[right]]:
                formed += 1
            
            # 3. While window valid (formed == required_chars), shrink
            while left <= right and formed == required_chars:
                # Update result if smaller
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    result = s[left:right+1]
                
                # Remove s[left] from window
                have[s[left]] -= 1
                if s[left] in need and have[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1

        return result
                
