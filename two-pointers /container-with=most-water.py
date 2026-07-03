# Problem : Container With Most Water
# Topic : Two Pointers

class Solution(object):
    def maxArea(self, height):
        n = len(height)
        i = 0
        j = n - 1
        Max = 0
        while i < j:
            Max = max(min(height[i],height[j])*(j - i),Max)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return Max
