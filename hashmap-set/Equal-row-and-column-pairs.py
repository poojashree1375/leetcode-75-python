# Problem : Equal Row and Column Pairs
# Topic : Hash Map / Set

# class Solution:
#     def equalPairs(self, grid: List[List[int]]) -> int:
#         cols = []
#         for j in range(len(grid)):
#             c = []
#             for i in range(len(grid)):
#                 c.append(grid[i][j])
#             cols.append(c)
#         count = 0
#         for i in grid:
#             if i in cols:
#                 count += cols.count(i)
#         return count

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = []
        for j in range(len(grid)):
            c = []
            for i in range(len(grid)):
                c.append(grid[i][j])
            cols.append(tuple(c))
        freq = {}
        for i in grid:
            if tuple(i) not in freq:
                freq[tuple(i)] = 1
            else:
                freq[tuple(i)] += 1
        count = 0
        for i in cols:
            if i in freq:
                count += freq[i]
        return count
