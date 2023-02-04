class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a = sorted(p)
        l = len(p)
        ls = []
        for i in range(len(s)-l+1):
            if sorted(s[i:i+l]) == a:
                ls.append(i)

        return ls
