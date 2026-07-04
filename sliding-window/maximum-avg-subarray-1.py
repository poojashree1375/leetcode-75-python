# Problem : Maximum Average Subarray I
# Topic : Sliding Window

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        Max = float('-inf')
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        Sum = 0
        for i in range(k):
            Sum += nums[i]
        Max = max(Sum/k, Max)
        left = 0
        right = k
        while right < len(nums):
            Sum = Sum - nums[left] + nums[right]
            Max = max(Sum/k, Max)
            left += 1
            right += 1
        return Max
