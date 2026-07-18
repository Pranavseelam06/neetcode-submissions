#keep moving if u see smt that appeared before keep it and rmeove the old thing
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = []
        highest = 0
        for i in range(len(s)):
            if s[i] in longest:
                highest = max(len(longest), highest)
                longest = longest[longest.index(s[i]) + 1:]
            longest.append(s[i])
        return max(len(longest), highest)