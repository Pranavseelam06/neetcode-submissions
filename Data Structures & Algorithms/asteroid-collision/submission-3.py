class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast_2 in asteroids:
            if not stack:
                stack.append(ast_2)
                continue

            while stack and stack[-1] > 0 and ast_2 < 0:
                ast_1 = stack[-1]

                if abs(ast_1) > abs(ast_2):
                    break
                elif abs(ast_1) == abs(ast_2):
                    stack.pop()
                    ast_2 = None
                    break
                else:
                    stack.pop()

            if ast_2 is not None:
                if not stack or not (stack[-1] > 0 and ast_2 < 0):
                    stack.append(ast_2)

        return stack