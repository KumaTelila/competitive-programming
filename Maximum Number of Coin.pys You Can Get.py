class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        c = 0
        i = len(piles) - 2
        n = len(piles)//3
        while(c<n and i>=0):
            c+=1
            res += piles[i]
            i-=2
        print(piles)
        return res