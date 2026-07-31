# We could have the first word and use the in feature
# and keep subtracting until one is found if size 
# becomes 0 just return. should be O(n)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        for i in range(len(strs)):
            while word and word not in strs[i]:
                word = word[:-1]
            if not word:
                return ""
        return word
        