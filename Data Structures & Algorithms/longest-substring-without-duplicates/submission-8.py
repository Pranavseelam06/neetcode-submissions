class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        place = {}
        left = 0
        size = 0

        for i in range(len(s)):
            if s[i] in place:
                size = max(size, i - left)
                left = max(left, place[s[i]] + 1)

            place[s[i]] = i

        return max(size, len(s) - left)