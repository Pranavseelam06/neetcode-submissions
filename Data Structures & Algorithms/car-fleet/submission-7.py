class Solution:
    def carFleet(self, target, position, speed):
        paired = sorted(zip(position, speed))
        print(paired)
        stack = []
        for p, s in paired:
            time = (target - p) / s
            while stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)
        return len(stack)