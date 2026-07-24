class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}

        for num in nums:
            seen[num]= seen.get(num,0)+1
        
        freq=[[] for i in range(len(nums)+1)]

        for index,number in seen.items():
            freq[number].append(index)

        result=[]

        for i in range(len(freq)-1,0,-1):
            for res in freq[i]:
                result.append(res)
            if len(result)==k:
                return result