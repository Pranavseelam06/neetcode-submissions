class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for i in range(len(strs)):
            sort = "".join(sorted(strs[i]))
            words[sort] = words.get(sort, [])
            words[sort].append(strs[i])
        return list(words.values())
