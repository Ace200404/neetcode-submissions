class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])

        count=0
        prev_count=float('-inf')

        for i in intervals:
            if i[0]<prev_count:
                count+=1
            else:
                prev_count=i[1]
        return count