"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time=defaultdict(int)

        for i in intervals:
            time[i.start]+=1
            time[i.end]-=1
        
        prev=0
        res=0

        for j in sorted(time.keys()):
            prev+=time[j]
            res=max(prev,res)
        return res