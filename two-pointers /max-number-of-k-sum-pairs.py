# Problem : Max Number of K-Sum Pairs
# Topic : Two Pointers

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        i = 0
        j = len(nums) - 1
        nums.sort()
        while i < j:
            if nums[i] + nums[j] == k:
                operations += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1
        return operations
