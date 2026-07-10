class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        max_count=0
        count=0
        n=len(nums)
        last_smallest=float("-inf")

        for i in range(0,n):
            num=nums[i]
            if num-1 == last_smallest:
                count=count+1
                last_smallest=num
            elif num != last_smallest:
                count=1
                last_smallest=num
            max_count=max(max_count,count)
        return max_count                          
