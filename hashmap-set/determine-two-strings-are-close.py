# Problem : Determine if Two Strings Are Close
# Topic : Hash Map / Set

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = {}
        for i in word1:
            if i not in freq1:
                freq1[i] = 1
            else:
                freq1[i] += 1
        freq2 = {}
        for i in word2:
            if i not in freq2:
                freq2[i] = 1
            else:
                freq2[i] += 1
        if sorted(freq1.keys()) == sorted(freq2.keys()) and sorted(freq1.values()) == sorted(freq2.values()):
            return True
        else:
            return False
