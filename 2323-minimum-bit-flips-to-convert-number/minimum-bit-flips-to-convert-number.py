class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        result=start^goal
        result=bin(result)
        return (result.count("1"))
        