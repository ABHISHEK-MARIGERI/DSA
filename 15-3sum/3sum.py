class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
     result=[]
     n= len(nums)
     nums.sort()

     for i in range(n-2):
        if i>0 and nums[i]==nums[i-1]:
            continue

        j=i+1
        k=n-1
        while j<k:
          if nums[i]+nums[j]+nums[k]<0:
             j=j+1
          elif nums[i]+nums[j]+nums[k]>0:
             k=k-1
          else:
             temp=[nums[i],nums[j],nums[k]]
             result.append(temp)
             j=j+1
             k=k-1

             while j<k and nums[j] == nums[j-1]:
                j=j+1
             while k>j and nums[k]== nums[k+1]:
                k=k-1   


     return result     
                     
