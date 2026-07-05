# Another solution for Find Pivot Index problem

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        right = 0
        for i in range(len(nums)):
            right = total - left - nums[i]
            if right == left:
                return i
            else:
                left += nums[i]
        return -1
