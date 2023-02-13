class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s = sum(cardPoints[:k])
        i = k-1
        j =len(cardPoints)-1
        m  = s
        while(i>=0):
            s = s-cardPoints[i]+cardPoints[j]
            m = max(m, s)
            i-=1
            j-=1
        return m
