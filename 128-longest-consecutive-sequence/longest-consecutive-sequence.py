class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

      my_set=set()
      for num in nums:
        my_set.add(num)

      max_count=0
      for num in my_set:
        if num-1 not in my_set:
            x=num
            count=1
            while x+1 in my_set:
                count+=1
                x+=1
            max_count=max(count,max_count)
      return max_count      
    

