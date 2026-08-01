

class Solution:
    def lowerBound(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n - 1
        lb = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1

        return lb

    def upperBound(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n - 1
        ub = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1

        return ub

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0:
            return [-1, -1]

        lb = self.lowerBound(nums, target)

        # Target does not exist
        if lb == -1 or nums[lb] != target:
            return [-1, -1]

        ub = self.upperBound(nums, target)

        # Target is the last element(s) in the array
        if ub == -1:
            return [lb, len(nums) - 1]

        return [lb, ub - 1]