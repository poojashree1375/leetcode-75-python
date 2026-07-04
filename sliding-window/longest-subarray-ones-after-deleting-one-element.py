# Problem : Longest Subarray of 1's After Deleting One Element
# Topic : Sliding Window

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        Max = 0
        zeros_count = 0
        while right < len(nums):
            if nums[right] == 0:
                zeros_count += 1
            while zeros_count > 1:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
            Max = max(right-left,Max)
            right += 1
        return Max
