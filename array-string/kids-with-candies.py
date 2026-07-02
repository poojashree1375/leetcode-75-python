# Problem : Kids With the Greatest Number of Candies
# Topic : Array / String

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        largest = max(candies)
        for i in candies:
            total = i + extraCandies
            if total >= largest:
                result.append(True)
            else:
                result.append(False)

        return result
