class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first store the nums and there count in a dict
        seen={}
        freq=[[]for i in range(len(nums)+1)]

        for num in nums:
            seen[num]=seen.get(num,0)+1
        # than set a list at index i to be the number 
        for index,value in seen.items():
            freq[value].append(index)


        # iterate through the list till you finish iterating over k
        result=[]
        for number in range(len(freq)-1,0,-1):
            for iteration in freq[number]:
                result.append(iteration)
            if len(result)==k:
                return result
        # return the result