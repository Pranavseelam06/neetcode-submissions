class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        dictionary = {'(':')','{':'}','[':']'}
        for i in range(len(s)):
            if s[i] in dictionary:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                if dictionary[stack.pop()] != s[i]:
                    return False
        if len(stack) != 0:
                    return False
        return True