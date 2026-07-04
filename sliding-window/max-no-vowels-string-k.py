# Problem : Maximum Number of Vowels in a Substring of Given Length
# Topic : Sliding Window

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        Max = 0
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        Max = max(count,Max)
        left = 0
        right = k
        while right < len(s):
            if s[left] in vowels:
                count -= 1
            if s[right] in vowels:
                count += 1
            Max = max(count,Max)
            left += 1
            right += 1
        return Max
