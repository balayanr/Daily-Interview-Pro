"""
This problem was recently asked by LinkedIn:

Given a 2-dimensional grid consisting of 1's (land blocks) and 0's (water blocks),
count the number of islands present in the grid. The definition of an island is as follows:
1.) Must be surrounded by water blocks.
2.) Consists of land blocks (1's) connected to adjacent land blocks
    (either vertically or horizontally).

Assume all edges outside of the grid are water.

Example:
Input:
10001
11000
10110
00000

Output: 3
"""
class Solution(object):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def inRange(self, grid, r, c):
        numRow, numCol = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= numRow or c >= numCol:
            return False
        return True

    def numIslands(self, grid):
        def mark_as_checked(grid, i, j):
            queue = [(i, j)]
            while queue:
                i, j = queue.pop(0)
                self.checked.add((i, j))
                for i_mod, j_mod in self.dirs:
                    if (i + i_mod, j + j_mod) not in self.checked and self.inRange(grid, i + i_mod, j + j_mod) and grid[i + i_mod][j + j_mod]:
                        queue.append((i + i_mod, j + j_mod))

        self.checked = set()
        counter = 0
        for i, row in enumerate(grid):
            for j, column in enumerate(row):
                if column and (i, j) not in self.checked:
                    mark_as_checked(grid, i, j)
                    counter += 1
                self.checked.add((i, j))
        return counter

grid = [[1, 0, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0]]
print(Solution().numIslands(grid))
# 3
