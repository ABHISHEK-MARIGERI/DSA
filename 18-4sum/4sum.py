class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        result=set()

        for i in range(0,n):
            for j in range(i+1,n):
                my_set=set()
                for k in range(j+1,n):
                    forth =target -(nums[i]+nums[j]+nums[k])
                    if forth in my_set:
                        temp=sorted([nums[i],nums[j],nums[k],forth])
                        result.add(tuple(temp))                   
                    my_set.add(nums[k])
        return [list(t) for t in result]                   

        