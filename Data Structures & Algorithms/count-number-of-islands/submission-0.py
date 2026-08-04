class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        def sink(i: int, j: int):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            sink(i - 1, j)
            sink(i + 1, j)
            sink(i, j - 1)
            sink(i, j + 1)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    sink(i,j)
        return count
