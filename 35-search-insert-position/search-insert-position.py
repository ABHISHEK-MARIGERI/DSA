class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        lb=-1
        low=0
        high=n-1

        while low <= high:
            mid=(low+high)//2

            if nums[mid]==target:
                lb=mid
                return lb
            elif nums[mid]<target:
                low=mid+1  
            else:
                high=mid-1   
        return low           
