class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        top = 0
        bottom = n - 1

        while top < bottom:
            for i in range(top, bottom):
                offset = i - top

                # save top-left value
                temp = matrix[top][i]

                # left -> top
                matrix[top][i] = matrix[bottom - offset][top]

                # bottom -> left
                matrix[bottom - offset][top] = matrix[bottom][bottom - offset]

                # right -> bottom
                matrix[bottom][bottom - offset] = matrix[i][bottom]

                # top -> right
                matrix[i][bottom] = temp

            top += 1
            bottom -= 1