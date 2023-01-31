class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)!=1:
            stones.sort()
            a = stones[-1]
            stones.pop()
            if(len(stones)!=0):
                b = stones[-1]
                stones.pop()
                stones.append(a-b)
            else:
                return stones[-1]
        return stones[-1]