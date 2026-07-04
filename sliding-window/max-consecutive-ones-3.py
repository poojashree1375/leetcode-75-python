# Problem : Max Consecutive Ones III
# Topic : Sliding Window

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        zeros_count = 0
        Max = 0
        while right < len(nums):
            if nums[right] == 0:
                zeros_count += 1
            while zeros_count > k:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
            if zeros_count <= k:
                Max = max(right-left+1, Max)
            right += 1
        return Max
