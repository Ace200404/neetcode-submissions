class Solution:
    
    def encode(self, strs: List[str]) -> str:
        rt=''

        for i in strs:
            rt+= str(len(i))+'#'+i
        return rt
        
    def decode(self, s: str) -> List[str]:
         rest=[]
         i=0
         while i < len(s):
            j=i
            while s[j]!='#':
                j+=1
            length= int(s[i:j])
            i = j+1
            j= i+ length
            rest.append(s[i:j])

            i=j
         return rest


        
        

        