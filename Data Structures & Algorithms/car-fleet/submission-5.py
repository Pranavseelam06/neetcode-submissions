class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = sorted(zip(position, speed), reverse=True)
        stack = deque()
        for i in range(len(paired)):
            if len(stack) == 0:
                time = (target - paired[i][0]) / paired[i][1]
                stack.append(time)
                continue
            time = (target - paired[i][0]) / paired[i][1]
            if stack and time > stack[-1]:
                stack.append(time)
        return len(stack)
                
                