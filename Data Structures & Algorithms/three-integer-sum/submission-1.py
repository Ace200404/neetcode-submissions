class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Sort the array first (crucial for avoiding duplicates and using two-pointer)

        Fix one element (nums[i]) at a time

        Use two-pointer on the remaining array to find pairs that sum to -nums[i]

        Use a set (or skip duplicates) to avoid duplicate triplets
        '''
        nums.sort()
        lst=[]

        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:

                if nums[left]+nums[right]==(-nums[i]):
                    if [nums[i],nums[left],nums[right]] not in lst:
                        lst.append([nums[i],nums[left],nums[right]])
                    right-=1
                    left+=1
                    continue

                if nums[left]+nums[right]>(-nums[i]):
                    right-=1
                else:
                    left+=1

        return lst