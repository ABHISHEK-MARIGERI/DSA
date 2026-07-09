class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        even=[]
        odd=[]
        for num in nums:
            if num>0:
                even.append(num)
            else:
                odd.append(num)

        n=len(even)
        arranged=[]
        i=0
        while i< n:
            arranged.append(even[i])
            arranged.append(odd[i])
            i+=1

        return arranged        