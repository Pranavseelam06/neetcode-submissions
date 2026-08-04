class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        max_size = 0
        self.current_count = 0
        def sink(i, j):
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0:
                return
            grid[i][j] = 0
            self.current_count += 1
            sink(i,j + 1)
            sink(i, j - 1)
            sink(i + 1, j)
            sink(i - 1, j)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    sink(i,j)
                    if self.current_count > max_size:
                        max_size = self.current_count
                    self.current_count = 0
        return max_size

