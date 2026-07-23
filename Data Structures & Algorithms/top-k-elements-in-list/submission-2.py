class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        freq=[[] for i in range(len(nums)+1)]

        for key,value in dic.items():
            freq[value].append(key)
        
        rs=[]
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                rs.append(j)
                if len(rs)==k:
                    return rs