class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        max_size = 0
        def sink(i, j) -> int:
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0:
                return 0
            size = 1
            grid[i][j] = 0
            size += sink(i,j + 1)
            size += sink(i, j - 1)
            size += sink(i + 1, j)
            size += sink(i - 1, j)
            return size

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    current_count = sink(i,j)
                    if current_count > max_size:
                        max_size = current_count
                    current_count = 0
        return max_size

