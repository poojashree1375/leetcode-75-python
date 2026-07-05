# Problem : Unique Number of Occurrences
# Topic : Hash Map / Set

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        return len(set(freq.values())) == len(freq.values())
