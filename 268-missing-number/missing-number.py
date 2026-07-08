class Solution:
    def missingNumber(self, nums: List[int]) -> int:
     n=len(nums)

     actual_sum=0
     for i in range(0,n+1):
        actual_sum+=i

     sum=0
     for num in nums:
        sum=sum+num

     return actual_sum - sum      

             