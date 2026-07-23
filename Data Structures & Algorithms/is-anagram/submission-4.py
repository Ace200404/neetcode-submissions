class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        letter_index={}

        for i in s:
            letter_index[i]= letter_index.get(i,0)+1
        
        for j in t:
            if j not in letter_index:
                return False
            letter_index[j]-=1
            if letter_index[j]==0:
                del letter_index[j]
        return True
            
