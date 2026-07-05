# Problem : Find the Highest Altitude
# Topic : Prefic Sum

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current= 0
        Max = 0
        for i in range(len(gain)):
            current += gain[i]
            Max = max(current,Max)
        return Max
