class Solution:
    def missingNumber(self, nums: List[int]) -> int:
     n=len(nums)
     d={}

     for i in range(0,n+1):
        d[i]=0

     for num in nums:
        d[num]+=1

     for i in range(0,n+1):
        if d[i]<1:
            return i         