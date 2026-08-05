class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        place = {}
        left = 0
        size = 0

        for right in range(len(s)):
            if s[right] in place:
                left = max(left, place[s[right]] + 1)
            place[s[right]] = right
            size = max(size, right - left + 1)
        return size