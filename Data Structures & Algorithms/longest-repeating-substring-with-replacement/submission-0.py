class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        window_length={}
        max_length=0
        freq_letter=0

        for right in range(len(s)):
            window_length[s[right]]= window_length.get(s[right],0)+1
            freq_letter=max(freq_letter,window_length[s[right]])
            
            while (right-left+1) - freq_letter > k:
                window_length[s[left]]-=1
                left+=1

            max_length=max(max_length, right-left+1)
        
        return max_length
               
             