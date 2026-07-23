class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # set a dictionary to get the value and number of iterations of each value
        seen={}
        freq=[[] for i in range(len(nums)+1)]
        for num in nums:
            seen[num]=seen.get(num,0)+1
        
        for number, count in seen.items():
            freq[count].append(number)

        result=[]
        for iteration in range(len(freq)-1,0,-1):
            for n in freq[iteration]:
                result.append(n)
                if len(result)==k:
                    return result
        
