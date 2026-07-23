class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count={}
        freq = [[] for i in range(len(nums)+1)]

        for x in nums:
            count[x]= 1+count.get(x,0)
        for key,value in count.items():
            freq[value].append(key)
        
        rest=[]

        for i in range(len(freq)-1,0,-1):
            for val in freq[i]:
                rest.append(val)
                if len(rest)==k:
                    return rest
        
        
