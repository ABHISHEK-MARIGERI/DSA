class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def find_left(target,nums):
            n=len(nums)
            low=0
            high=n-1

            while low<=high:
                mid=(low+high)//2
                if nums[mid] >= target:
                    high=mid-1
                else:
                    low=mid+1

            return low


        def find_right(target,nums):
            n=len(nums)
            low=0
            high=n-1

            while low <= high:
                mid=(low+high)//2
                if nums[mid] == target:
                    low=mid+1
                elif nums[mid] < target:
                    low = mid+1
                else:
                    high=mid-1
            return high


        left_most_element = find_left(target,nums)
        right_most_element = find_right(target,nums)


        if left_most_element <= right_most_element:
            return [left_most_element,right_most_element]
        else:
            return [-1,-1]    


        