class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        
        def bs(nums,target,low,high):
            if low>high:return -1
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                return bs(nums,target,mid+1,high)
            else:
                return bs(nums,target,low,mid-1)        


        return bs(nums,target,0,n-1)