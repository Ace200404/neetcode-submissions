class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars=[]

        for pos, spd in zip(position,speed):
            time=(target-pos)/spd
            cars.append((pos,spd,time))
        
        cars.sort(key=lambda x:x[0],reverse=True)
        stack=[]
        for i in cars:
            if stack and stack[-1][2]>=i[2]:
                continue
            stack.append(i)
        return len(stack)
