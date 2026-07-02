# Problem : Reverse Words in a String
# Topic : Array / String

class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        for word in s.strip().split():
            words.append(word)
        words.reverse()
        return " ".join(words)
