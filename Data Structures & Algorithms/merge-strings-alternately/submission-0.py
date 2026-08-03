class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = ""
        length_word2 = len(word2)
        for i in range(len(word1)):
            new_string += word1[i]
            if i < length_word2:
                new_string += word2[i]
        new_string += word2[len(word1):]
        return new_string