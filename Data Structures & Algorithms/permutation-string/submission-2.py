class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target=Counter(s1)
        print(target,'target')
        for right in range(len(s2)-len(s1)+1):
            
            window = Counter(s2[right:right+len(s1)])
            print(window,"window")
            if window==target:
                return True 
        return False
            

            