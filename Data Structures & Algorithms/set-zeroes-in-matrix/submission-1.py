class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def makeZero(i: int, j: int) -> None:
            for row in range(len(matrix)):
                if matrix[row][j] != 0:
                    matrix[row][j] = None
            for col in range(len(matrix[0])):
                if matrix[i][col] != 0:
                    matrix[i][col] = None

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    makeZero(i, j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] is None:
                    matrix[i][j] = 0