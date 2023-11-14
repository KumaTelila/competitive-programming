class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        merged = ''
        while i<len(word1) and j < len(word2):
            if word1[i] > word2[j]:
                merged+=word1[i]
                i+=1
            elif word1[i] < word2[j]:
                merged+=word2[j]
                j+=1
            else:
                rest_1 = word1[i:]
                rest_2 = word2[j:]
                if rest_1 > rest_2:
                    merged+=word1[i]
                    i+=1
                else:
                    merged+=word2[j]
                    j+=1
        while j < len(word2):
            merged+=word2[j]
            j+=1
        while i < len(word1):
            merged+=word1[i]
            i+=1
        return merged       