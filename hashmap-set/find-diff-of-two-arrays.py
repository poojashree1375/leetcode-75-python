# Problem : Find the Difference of Two Arrays
# Topic : Hash Map / Set

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1 = set(nums1)
        n2 = set(nums2)
        answer = []
        answer.append(list(n1-n2))
        answer.append(list(n2-n1))
        return answer
