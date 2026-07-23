class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        highest_area=0
        stack=[]

        for i, h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                index, height=stack.pop()
                highest_area=max(highest_area,height*(i-index))
                start= index
            stack.append((start,h))
        for i, h in stack:
            highest_area=max(highest_area, h*(len(heights)-i))
        return highest_area