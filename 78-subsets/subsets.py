class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        no_of_subsets=2**n

        result=[]
 

        for num in range(0,no_of_subsets):
            list=[]
            for i in range(n):
                if num & (1<<i)!=0:
                 list.append(nums[i])
            result.append(list)
        return result        


        