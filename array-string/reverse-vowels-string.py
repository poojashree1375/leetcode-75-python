# Problem : Reverse Vowels of a String
# Topic : Array / String

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        result = []
        for i in s:
            if i.lower() in ['a','e','i','o','u']:
                vowels.append(i)
        vowels.reverse()
        i = 0
        for c in s:
            if c.lower() in ['a','e','i','o','u']:
                result.append(vowels[i])
                i += 1
            else:
                result.append(c)
        return "".join(result)
